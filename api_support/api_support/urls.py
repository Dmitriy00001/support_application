from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/authorization/', include('api_support_authorization.urls')),
    path('api/chat/', include('api_support_chat.urls'))
]


