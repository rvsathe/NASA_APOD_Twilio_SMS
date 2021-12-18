from celery.utils.log import get_task_logger
from celery import app
from celery import shared_task
from dotenv import load_dotenv
load_dotenv()
import os

from django.db import models
from twilio.rest import Client
from .sms_sender import send_sms

logger = get_task_logger(__name__)


@shared_task
def send_sms_from_twilio_number_task():
    logger.info(f"Sent the sms")
    return send_sms()
