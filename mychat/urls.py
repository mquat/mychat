from django.urls.conf import include
from django.urls import path

urlpatterns = [
    path('chat/', include('chat.urls')),
]
