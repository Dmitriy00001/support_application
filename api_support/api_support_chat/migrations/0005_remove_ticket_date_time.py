# Generated by Django 3.2.8 on 2021-10-26 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_support_chat', '0004_alter_ticket_status_ticket'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='date_time',
        ),
    ]