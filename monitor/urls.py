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
