"""PRIO_test1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from PRIO_test1.views import webPage_1, webPage_2, webPage_3

urlpatterns = [
    path('admin/', admin.site.urls),
    path("Dashboard/", webPage_1, name="webPage_1"),
    path("AddTask/", webPage_2, name="webPage_2"),
    path("AddSub/", webPage_3, name="webPage_3"),
]
