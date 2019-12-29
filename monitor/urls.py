"""monitor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from . import views

app_name = 'monitor'

urlpatterns = [
    path('',views.index, name="home"),
    path('error/', views.error_msg, name="error"),
    path('subscriber_list',views.add_or_view_subscriber,name="subscriber_list"),
    path('add_subscriber/',views.add_or_view_subscriber,name="add_subscriber"),
    path('get_metrics/',views.get_cpu_utilization,name="get_metrics"),
    path('sendmail/',views.sendmail,name="sendmail"),
    path('admin/', admin.site.urls),
]
