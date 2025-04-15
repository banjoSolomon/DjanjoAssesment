from celery import shared_task
import time


@shared_task
def process_data(email, message):
    time.sleep(10)  # Simulating delay
    return f"Processed email to {email} with message: {message}"
