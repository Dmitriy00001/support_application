# Generated by Django 3.2.8 on 2021-10-26 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_support_chat', '0002_alter_ticket_creator_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status_ticket',
            field=models.IntegerField(choices=[(1, 'Нерешенный'), (2, 'Решенный'), (3, 'Замороженный')], default=1, max_length=1),
        ),
    ]