from django.conf.urls import url

from .views import Display,send

urlpatterns = [
        url('ass/', Display.as_view(), name='gallary'),
        url('post/',send, name='post')
]
