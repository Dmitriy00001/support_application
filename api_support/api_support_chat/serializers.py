from rest_framework import serializers
from api_support_chat.models import Ticket, Message


class TicketCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['ticket_name']


class MessageCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['ticket', 'message']


class TicketListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id', 'ticket_name', 'creator_name', 'status_ticket')


class UserTicketListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('ticket', 'author_message', 'message')


class SupportTicketListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['ticket', 'message']


class TicketStatusUpdateViewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['status_ticket']
