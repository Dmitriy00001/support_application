from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from .models import Ticket, Message
from .serializers import TicketCreateSerializers, TicketListSerializers, MessageCreateSerializers, \
    UserTicketListSerializers, TicketStatusUpdateViewSerializers, SupportTicketListSerializers


class TicketCreateView(generics.CreateAPIView):
    """
            1)Создание тикета.
            2)Имеет доступ только авторизованный пользователь.
    """
    serializer_class = TicketCreateSerializers
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.validated_data['creator_name'] = self.request.user
        serializer.save()


class MessageCreateView(generics.CreateAPIView):
    """
            1)Создание сообщения.
            2)Имеет доступ авторизованный пользователь.
            3)Имеет доступ Support.
    """
    serializer_class = MessageCreateSerializers
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.validated_data['author_message'] = self.request.user
        serializer.save()


class TicketListView(ModelViewSet):
    """
            1)Получение списка всех созданных тикетов.
            2)Имеет возможность фильтрации по [названию тикета, имени создателя тикета, cтатусу и id].
            3)Имеет доступ только Support.

    """
    permission_classes = [IsAdminUser, ]
    serializer_class = TicketListSerializers
    queryset = Ticket.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['ticket_name', 'creator_name', 'status_ticket', 'id']


class SupportTicketListView(ModelViewSet):
    """
            1)Получение списка всех сообщений.
            2)Имеет возможность получения всех сообщений для конкретного тикета.
            3)Имеет доступ только Support.
    """
    permission_classes = [IsAdminUser, ]
    serializer_class = UserTicketListSerializers
    queryset = Message.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['ticket']


class UserTicketListView(ModelViewSet):
    """
            1)Получение списка всех сообщений пользователем,
            относящихся к созданным им тикетов.
            3)Имеет возможность выбора конкретного тикета.
            2)Имеет доступ только авторизованный пользователь.
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
            1)Изменение статуса тикета.
            2)Имеет возможность выбора конкретного тикета.
            3)Имеет доступ только Support.
    """
    serializer_class = TicketStatusUpdateViewSerializers
    queryset = Ticket.objects.all()
    permission_classes = [IsAdminUser,]



