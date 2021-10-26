from django.urls import path
from .views import Display,send,home,Detail

urlpatterns = [
        path('home/', home, name='home'),
        path('browse/', Display.as_view(), name='gallary'),
        path('post/',send.as_view(), name='post'),
        path('<int:pk>/detail/', Detail.as_view(), name='detail'),
]
