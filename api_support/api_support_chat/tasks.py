from celery import shared_task
from .models import Message


@shared_task()
def get_all_message():
    obj_name = Message.objects.get(id=70)
    print(obj_name)







