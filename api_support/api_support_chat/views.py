from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from api_support_chat.models import Ticket, Message
from api_support_chat.serializers import TicketCreateSerializers, TicketListSerializers, MessageCreateSerializers, \
    UserTicketListSerializers, TicketStatusUpdateViewSerializers, SupportTicketListSerializers


class TicketCreateView(ModelViewSet):
    """
            1)Creating a ticket.
            Access:Only authorized user.
    """
    serializer_class = TicketCreateSerializers
    queryset = Ticket.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.validated_data['creator_name'] = self.request.user
        serializer.save()


class MessageCreateView(ModelViewSet):
    """
            1)Create a message.
            Access:Authorized user.
            Access:Support manager.
    """
    serializer_class = MessageCreateSerializers
    queryset = Message.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.validated_data['author_message'] = self.request.user
        serializer.save()


class TicketListView(ModelViewSet):
    """
            1)Get all created tickets.
            2)Has a filter by [ticket name, ticket creator name, status and id].
            Access:Support manager.

    """
    permission_classes = [IsAdminUser, ]
    serializer_class = TicketListSerializers
    queryset = Ticket.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['ticket_name', 'creator_name', 'status_ticket', 'id']


class SupportTicketListView(ModelViewSet):
    """
            1)Get all created messages.
            2)Get all messages for a specific ticket.
            Access:Support manager.
    """
    permission_classes = [IsAdminUser, ]
    serializer_class = UserTicketListSerializers
    queryset = Message.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['ticket']


class UserTicketListView(ModelViewSet):
    """
            1)Receiving all messages,related to the user.
            2)Selection of a specific ticket.
            Access:Only authorized user.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = SupportTicketListSerializers
    queryset = Message.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['ticket']

    def get_queryset(self):
        owner_queryset = self.queryset.filter(ticket__creator_name=self.request.user)
        return owner_queryset


class TicketStatusUpdateView(generics.RetrieveUpdateDestroyAPIView):
    """
            1)Change ticket status.
            2)Selection of a specific ticket.
            Access:Only support manager.
    """
    serializer_class = TicketStatusUpdateViewSerializers
    queryset = Ticket.objects.all()
    permission_classes = [IsAdminUser, ]



