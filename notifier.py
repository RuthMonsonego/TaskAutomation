import smtplib
from email.mime.text import MIMEText
import requests
from config import MAILGUN_SETTINGS, MANAGER_EMAIL

def send_email(recipient, subject, body):
    response = requests.post(
        f"https://api.mailgun.net/v3/{MAILGUN_SETTINGS['domain']}/messages",
        auth=("api", MAILGUN_SETTINGS["api_key"]),
        data={
            "from": f"Task Automation <mailgun@{MAILGUN_SETTINGS['domain']}>",
            "to": [recipient],
            "subject": subject,
            "text": body,
        },
    )
    if response.status_code == 200:
        print(f"Email sent to {recipient}.")
    else:
        print(f"Error sending email to {recipient}: {response.status_code}, {response.text}")

def send_alert(customer, task):
    subject = f"Task '{task}' in progress"
    body = f"Hello {customer['name']},\n\nYour task '{task}' is currently in progress."
    send_email(customer["email"], subject, body)

def send_summary_report(report_file):
    subject = "Task Summary Report"
    body = "Attached is the summary report of the last 10 tasks completed in the system."

    with open(report_file, "r") as file:
        report_content = file.read()

    msg = MIMEText(body + "\n\n" + report_content)
    msg['Subject'] = subject
    msg['From'] = f"Task Automation <mailgun@{MAILGUN_SETTINGS['domain']}>"
    msg['To'] = MANAGER_EMAIL

    with smtplib.SMTP(MAILGUN_SETTINGS["smtp_server"], MAILGUN_SETTINGS["smtp_port"]) as server:
        server.starttls()
        server.login(MAILGUN_SETTINGS["api_key"], MAILGUN_SETTINGS["api_key"])
        server.sendmail(msg['From'], [msg['To']], msg.as_string())
    print("Summary report sent to the manager.")
