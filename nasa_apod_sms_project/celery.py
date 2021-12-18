from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE','nasa_apod_sms_project.settings')
app = Celery('nasa_apod_sms_project')

app.config_from_object('django.conf:settings')

app.conf.beat_schedule = {
    'everyday-9am':{
        'task': 'twilio_sms.tasks.send_sms_from_twilio_number_task',
        'schedule': crontab(hour='9',minute='30'),
    }
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))