"""
URL configuration for ahui_proyecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
"""
from django.contrib import admin
from django.urls import path
from App1 import views as app1
from App2 import views as app2


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Vista1/', app1.vista1),
    path('Vista2/', app1.vista2),
    path('Vista1/', app2.vista1),
    path('Vista2/', app2.vista2),
]
