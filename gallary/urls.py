from django.conf.urls import url

from .views import Display,send,home

urlpatterns = [
        url('home/', home, name='home'),
        url('browse/', Display.as_view(), name='gallary'),
        url('post/',send.as_view(), name='post'),
]
