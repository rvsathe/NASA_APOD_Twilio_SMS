""" Makes the call to the NASA APOD API and stores the picture in the model"""

import json
from django.http.response import HttpResponse
import requests
import os
import pytz
from .models import SMS
from django.db import models
from twilio.rest import Client
from datetime import datetime
from datetime import date
from django.forms.models import model_to_dict


def get_nasa_apod_from_api():

    nasa_api_key= os.getenv("NASA_APOD_API_KEY")
    my_timezone = pytz.timezone('America/Los_Angeles')
    current = datetime.now(tz=my_timezone).strftime('%Y-%m-%d')
    response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={nasa_api_key}&date={current}')
    response_json = response.json()
    
    if not SMS.objects.filter(title=response_json['title']).exists():
        sms_obj = SMS(
            title=response_json['title'],
            image_url=response_json['url'],
            description=response_json['explanation']
        )
        sms_obj.save()
        return sms_obj

    query_result = SMS.objects.latest("created_on")
    final_obj = model_to_dict( query_result )

    return final_obj