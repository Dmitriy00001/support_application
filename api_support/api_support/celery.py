import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_support.settings')

app = Celery('api_support')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'get-objects': {
        'task': 'api_support_chat.tasks.get_all_message',
        'schedule': 15.0
    }
}