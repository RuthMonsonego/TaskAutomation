# Python Automation System for Task Management

This project is a Python-based dynamic automation system that handles task management through HTTP requests. The system receives tasks, processes them based on urgency, and provides notifications to customers and administrators. Logs are printed throughout the process to notify about the system's state and task progress.

## System Overview

The system works as follows:

1. **Receiving Tasks**: New tasks are received dynamically through HTTP requests and added to a queue as pending tasks.
2. **Priority-Based Processing**: The system processes tasks based on their urgency level. Tasks with the same urgency are processed in the order they were received (FIFO).
3. **Task Execution**: Each task is executed for 1 minute (simulating task completion).
4. **Task Completion**: Once a task is completed, its status is updated to "Completed," and an email is sent to the customer.
5. **Continuous Processing**: The system continues processing tasks one by one, pulling the next task from the queue and executing it.
6. **Report Generation**: After every 10 completed tasks, a summary report is sent to the administrator via email.
7. **Logging**: The system prints logs throughout its operation to notify the state of the system and track task progress.

## Features

- **Dynamic Task Reception**: The system receives tasks through HTTP requests and adds them to a priority queue.
- **Priority Task Execution**: Tasks are processed based on urgency and the order they were received.
- **Automated Email Notifications**: Once a task is completed, an email is sent to the associated customer. Every 10 tasks, a summary report is emailed to the administrator.
- **Logging**: Logs are printed to notify the system’s state and the status of tasks being processed.

## Project Structure

- `app.py`: Main Flask application that manages task reception and execution.
- `notifier.py`: Handles email notifications and summary report generation.
- `queue_manager.py`: Implements a priority queue for managing tasks.
- `customer.py`: Handles customer data and retrieves customers by ID.
- `reports.py`: Generates CSV reports for the completed tasks.
- `config.py`: Contains the configuration settings for the Mailgun API and email service.

## Requirements

- Python 3.7+
- Flask
- Requests
- Pandas
- smtplib (for sending emails)

## Installation

1. Clone the repository:

   git clone https://github.com/yourusername/task-automation.git
   cd task-automation
   
2. Create a virtual environment (optional but recommended):

  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install the required packages:

  pip install -r requirements.txt

4. Set up the Mailgun API keys in config.py:

  MAILGUN_SETTINGS = {
    "api_key": "your-api-key",
    "domain": "your-mailgun-domain"
  }

5. Ensure you have the following directory structure:

  /output

  The reports will be saved in this directory.

## Usage

1. Start the Flask server:

  python app.py

2. You can add tasks by making a POST request to the /add_task endpoint with the following JSON body:

  {
    "customer_id": 1,
    "task": "Task Description",
    "priority": 1
  }

  Example using curl:

  curl -X POST -H "Content-Type: application/json" -d '{"customer_id": 1, "task": "Complete Task", "priority": 1}' http://localhost:5000/add_task

3. The system will process tasks in the background, send notifications to customers when tasks are in progress or completed, and send summary reports to the administrator after every 10 tasks.

4. Logs will be printed to the console to show the current status of tasks and the system.

