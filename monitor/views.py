import psutil, os, platform, re
import subprocess as k

from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Subscriber
from . forms import SubscriberForm

recievers = []
def index(request):
    """ Home page and auto added recievers while triggered for mail """
    for subscriber in Subscriber.objects.all():
        recievers.append(subscriber.mail)
    return render(request,'index.html')


@api_view(['GET'])
def get_cpu_utilization(request):
    """ Fetching realtime CPU and RAM usage """

    if platform.system() == "Windows":
        cpu_cmd = k.run(['wmic', 'cpu', 'get', 'loadpercentage'],capture_output=True)
        cpu_percent = float(re.search(r'\d+',cpu_cmd.stdout.decode()).group())
        ram_percent = psutil.virtual_memory().percent
        return Response({'cpu_percent':cpu_percent, 'ram_percent':ram_percent})
    elif platform.system() == "Linux":
        cpu_cmd = "mpstat | awk '$3 ~ /CPU/ { for(i=1;i<=NF;i++) { if ($i ~ /%idle/) field=i } } $3 ~ /all/ { print 100 - $field }'"
        cpu_percent = str(os.popen(cpu_cmd).read())[:-2]
        ram_percent = psutil.virtual_memory().percent
        return Response({'cpu_percent':cpu_percent, 'ram_percent':ram_percent})

def error_msg(request):
    """ If error Occured then auto triggered this page """
    return render(request,'error_page.html')

def sendmail(request):
    """ sending realtime notifications using sendgrid """
    check = send_mail('CPU Memory Low Alert', 'CPU usage more than 50%.', 'mail@example.com',recievers, fail_silently=False)
    if check:
        return HttpResponse('done')
    else:
        return HttpResponse('Not Done')
    

def add_or_view_subscriber(request):
   """ List all subscribers , or create a new subscriber. """
   if request.method == 'POST':
       subscriber = SubscriberForm(request.POST)
       if subscriber.is_valid() and subscriber.clean_email() :
          subscriber.save()
          return redirect('subscriber_list')
       return redirect('error')
   else:
      subscribers = Subscriber.objects.all()
      return render(request,'subscriber_list.html',context={'subscribers':subscribers})


