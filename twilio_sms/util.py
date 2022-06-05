""" Makes the call to the NASA APOD API and stores the picture in the model"""

import json
from django.http.response import HttpResponse
import requests
import os
import pytz
from .models import SMS
import datetime
from datetime import datetime
from datetime import timedelta
from django.forms.models import model_to_dict


def get_final_sms_object():
    my_timezone = pytz.timezone('America/New_York')
    try:   
       current = datetime.now(tz=my_timezone).strftime('%Y-%m-%d')
       response_json = get_nasa_apod_from_api(current)
       sms_obj = SMS(
            title=response_json['title'],
            image_url=response_json['url'],
            description=response_json['explanation']
        )
       sms_obj.save()   
    except KeyError:
        yesterday = datetime.strptime(current.replace("-",""), "%Y%m%d").date() - timedelta(days = 1)
        response_json = get_nasa_apod_from_api(yesterday)
        sms_obj = SMS(
            title=response_json['title'],
            image_url=response_json['url'],
            description=response_json['explanation']
        )
        sms_obj.save()
    return model_to_dict(sms_obj)

def get_nasa_apod_from_api(current):
    nasa_api_key= os.getenv("NASA_APOD_API_KEY")
    response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={nasa_api_key}&date={current}')
    response_json = response.json()
    return response_json