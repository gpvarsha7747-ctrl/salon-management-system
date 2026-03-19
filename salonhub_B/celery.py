import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'salonhub_B.settings')

app = Celery('salonhub_B')
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
