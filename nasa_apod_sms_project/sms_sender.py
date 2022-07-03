from dotenv import load_dotenv
load_dotenv()
import os
import json
from django.http.response import HttpResponse
import requests
import pytz
from twilio.rest import Client
import datetime
from datetime import datetime

def send_sms(*args, **kwargs):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_TOKEN")
    my_twilio_number = os.getenv("TWILIO_NUMBER")
    receiver_number = os.getenv("RECEIVER_NUMBER")

    client = Client(account_sid, auth_token)
    
    sms = get_message_object()

    title = sms['title']
    picture = sms['hdurl'] 
    explanation = sms['explanation']

    message = client.messages.create(
            body=f'Today\'s picture is of: {title}! \n\n Description of Photo:{explanation}',
            from_=my_twilio_number,
            media_url=[f'{picture}'],
            to=receiver_number,
    )
    print(message.sid)
    

def get_message_object():
    my_timezone = pytz.timezone('America/New_York')
    nasa_api_key =  os.getenv("NASA_APOD_API_KEY")
 
    current = datetime.now(tz=my_timezone).strftime('%Y-%m-%d')
    response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={nasa_api_key}&date={current}')
    return response.json()
