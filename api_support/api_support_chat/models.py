from django.db import models
from django.contrib.auth.models import User


class Ticket(models.Model):
    ticket_name = models.CharField(max_length=255, verbose_name='Ticket name')
    creator_name = models.ForeignKey(User, verbose_name='Ticket creator', on_delete=models.SET_NULL,
                                     null=True, related_name='related_creator')
    support_manager_name = models.ForeignKey(User, verbose_name='Support manager', on_delete=models.CASCADE,
                                             related_name='related_support', default=User.objects.get(is_staff=True))
    TICKET_CHOICES = [
        (1, 'Active'),
        (2, 'Inactive'),
        (3, 'Frozen'),
    ]
    status_ticket = models.IntegerField(max_length=1, choices=TICKET_CHOICES, default=1, verbose_name='Ticket status')

    def __str__(self):
        return f"""ID:{self.id} Ticket name: {self.ticket_name} Ticket creator: {self.creator_name}"""


class Message(models.Model):
    ticket = models.ForeignKey(Ticket, verbose_name="Ticket", on_delete=models.CASCADE)
    author_message = models.ForeignKey(User, verbose_name="Post author", on_delete=models.CASCADE)
    message = models.TextField(verbose_name="Message text")

    def __str__(self):
        return f"""ID:{self.id} Message text: {self.message} Apply to a ticket ID:{self.ticket.id}"""
