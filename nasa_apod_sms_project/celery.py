from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from celery import shared_task

os.environ.setdefault('DJANGO_SETTINGS_MODULE','nasa_apod_sms_project.settings')
app = Celery('nasa_apod_sms_project')

app.config_from_object('django.conf:settings')

app.conf.beat_schedule = {
    'everyday-9.00am':{
        'task': 'twilio_sms.tasks.send_sms_from_twilio_number_task',
        'schedule': crontab(minute='00',hour='09'), ## (minute='*/5') # every five minutes
    }
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
