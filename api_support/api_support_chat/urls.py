from django.urls import path
from rest_framework.routers import SimpleRouter
from api_support_chat.views import \
    TicketCreateView,\
    TicketListView,\
    MessageCreateView,\
    UserTicketListView,\
    TicketStatusUpdateView,\
    SupportTicketListView

router = SimpleRouter()
router.register('get/all/message', SupportTicketListView)
router.register('message/get/all', UserTicketListView)
router.register('ticket/get/all', TicketListView)
router.register('ticket/create', TicketCreateView)
router.register('message/create', MessageCreateView)

urlpatterns = [
    path('ticket/put/status/<int:pk>/', TicketStatusUpdateView.as_view())
]
urlpatterns += router.urls
