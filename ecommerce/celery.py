from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from settings import celery

# set the default Django settings module for the 'celery' program.
# in this case the settings we are using are located in config.settings
# so make sure you point to the correct path
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery('config')

# Using a string here means the worker don't have to serialize
# the config object to child processes.
# - namespace='CELERY' means all celery-related config keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
