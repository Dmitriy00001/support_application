from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import TicketCreateView, TicketListView, MessageCreateView, UserTicketListView, TicketStatusUpdateView, \
    SupportTicketListView

router = SimpleRouter()
router.register('get/all/message', SupportTicketListView)
router.register('message/get/all', UserTicketListView)
router.register('ticket/get/all', TicketListView)

urlpatterns = [
    path('ticket/create', TicketCreateView.as_view()),
    path('message/create', MessageCreateView.as_view()),
    path('ticket/put/status/<int:pk>/', TicketStatusUpdateView.as_view())
]
urlpatterns += router.urls
