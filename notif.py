from celery import Celery
from app import *
celery = Celery('app', broker='redis://localhost:6379/0')

from celery import shared_task
from datetime import datetime, time
import requests

@shared_task
def send_reminder(user_id):
    now = datetime.now().time()
    user_obj=User.query.filter_by(user_id=user_id)
    if user_obj:
        last_visited=user_obj.last_logged
        if now > time(hour=18):

        # Check if the user has visited/posted anything
        # You can use the requests library to make API calls to your Flask app to check if the user has visited/posted anything

        # If the user has not visited/posted anything, send the alert
        # You can use the requests library to send the alert using webhook, SMS or email
