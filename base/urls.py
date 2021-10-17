"""base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
To add and render pictures:
    1. Create an ImageField in the model
    2. Register app for admin and create some data
    3. Import settings from django.conf
        and static from django.conf.urls.static

        ( 
          from django.conf import settings

          from django.conf.urls.static import static
        )

    4. Paste this snippet at the bottom:
        urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include,path
from django.conf.urls.static import static    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('gallary/', include('gallary.urls'))
]

urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
