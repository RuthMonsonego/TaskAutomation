from flask import Flask, request, jsonify
from queue_manager import PriorityQueue
from notifier import send_alert
from reports import generate_report
from customer import get_customer_by_id
import pandas as pd
import time
import threading

app = Flask(__name__)

# Create a queue for task execution
queue = PriorityQueue()
processed_tasks = []  # Completed tasks

# Function for processing tasks
def process_tasks():
    while True:
        if not queue.is_empty():
            # Retrieve a task from the queue
            task = queue.pop_task()
            task["status"] = "In Progress"
            print(f"Processing task: {task['task']} for {task['client_name']}")
            # Wait for one minute (represents execution time)
            time.sleep(60)
            task["status"] = "Completed"
            processed_tasks.append(task)
            send_alert(task["customer"], task["task"])
            print(f"Task for {task['client_name']} completed")
            
            # Send a report to the manager every 10 tasks
            if len(processed_tasks) % 10 == 0:
                generate_report(processed_tasks, "./output/report.csv")

        time.sleep(1)  # Wait one second before checking for another task

# Function to add a task
@app.route('/add_task', methods=['POST'])
def add_task():
    data = request.json
    
    # Retrieve customer details by customer ID
    customer = get_customer_by_id(data["customer_id"])
    
    if customer is None:
        return jsonify({"message": "Customer not found"}), 404
    
    # Create the task
    task = {
        "client_name": customer.name,
        "client_email": customer.email,
        "task": data["task"],
        "priority": data["priority"],
        "status": "Waiting"  # Queue status
    }
    
    # Add the task to the queue
    queue.add_task(task, task["priority"], customer)
    print(f"Task added: {task['task']} for {task['client_name']}")
    return jsonify({"message": "Task added successfully"}), 200

# Start the server
if __name__ == "__main__":
    # Run the task processing process in the background
    threading.Thread(target=process_tasks, daemon=True).start()
    app.run(debug=True)
