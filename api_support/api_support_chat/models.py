from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):
    ticket_name = models.CharField(max_length=255, verbose_name='Название тикета')
    creator_name = models.ForeignKey(User, verbose_name='Создатель тикета', on_delete=models.SET_NULL,
                                     null=True, related_name='related_creator')
    support_manager_name = models.ForeignKey(User, verbose_name='Менеджер службы поддержки', on_delete=models.CASCADE,
                                             related_name='related_support', default=User.objects.get(is_staff=True))
    TICKET_CHOICES = [
        (1, 'Нерешенный'),
        (2, 'Решенный'),
        (3, 'Замороженный'),
    ]
    status_ticket = models.IntegerField(max_length=1, choices=TICKET_CHOICES, default=1, verbose_name='Статус тикета')

    def __str__(self):
        return f"""ID:{self.id} НАЗВАНИЕ ТИКЕТА: {self.ticket_name} СОЗДАТЕЛЬ ТИКЕТА: {self.creator_name}"""


class Message(models.Model):
    ticket = models.ForeignKey(Ticket, verbose_name="Тикет", on_delete=models.CASCADE)
    author_message = models.ForeignKey(User, verbose_name="Автор сообщения", on_delete=models.CASCADE)
    message = models.TextField(verbose_name="Текст сообщения")

    def __str__(self):
        return f"""ID:{self.id} ТЕКС СООБЩЕНИЯ: {self.message} ОТНОСИТЬСЯ К ТИКЕТУ ID:{self.ticket.id}"""
