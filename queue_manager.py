import time
import heapq
import threading
from customer import Customer
from notifier import send_summary_report

class PriorityQueue:
    def __init__(self):
        self.queue = []  # Queue of pending tasks
        self.processing = False  # Variable to check if a task is being processed
        self.completed_tasks = 0  # Counter for completed tasks

    def add_task(self, task, priority, customer):
        # Assign customer details to the task
        task["customer"] = {"name": customer.name, "email": customer.email}
        order = len(self.queue)  # Preserve task order
        heapq.heappush(self.queue, (priority, order, task))
        print(f"New task added: {task['task']} for {task['customer']['name']}")

    def pop_task(self):
        if self.is_empty():
            return None

        # If no task is being processed, get the first task in the queue
        if not self.processing:
            self.processing = True  # Mark that we started processing a task
            priority, order, task = heapq.heappop(self.queue)
            task["status"] = "In Progress"
            print(f"New task added: {task['task']} for {task['customer']['name']}")
            
            # Wait for one minute to complete the task
            time.sleep(60)
            task["status"] = "Completed"
            self.processing = False  # End task processing
            self.completed_tasks += 1
            print(f"New task added: {task['task']} for {task['customer']['name']}")

            # After every 10 tasks
            if self.completed_tasks % 10 == 0:
                send_summary_report("./output/report.csv")  # Send a report to the manager

            return task

        # If a task is being processed, return and wait
        return None

    def is_empty(self):
        return len(self.queue) == 0