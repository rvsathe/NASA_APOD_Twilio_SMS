from dotenv import load_dotenv
load_dotenv()
import os

from django.db import models
from twilio.rest import Client
from .util import get_nasa_apod_from_api

def send_sms(*args, **kwargs):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_TOKEN")
    my_twilio_number = os.getenv("TWILIO_NUMBER")
    receiver_number = os.getenv("RECEIVER_NUMBER")

    client = Client(account_sid, auth_token)

    sms_obj = get_nasa_apod_from_api()

    title = sms_obj['title']
    picture = sms_obj['image_url'] 
    explanation = sms_obj['description']

    message = client.messages.create(
            body=f'Today\'s picture is of: {title}! \n\n Description of Photo:{explanation}',
            from_=my_twilio_number,
            media_url=[f'{picture}'],
            to=receiver_number,
    )
    print(message.sid)