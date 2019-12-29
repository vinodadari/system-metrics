import psutil, os, platform, re
import subprocess as k

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.core.mail import send_mail

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from . serializers import SubscriberSerializer
from . models import Subscriber
def index(request):
    return render(request,'index.html')

def add_metrics(request):
    pass

@api_view(['GET'])
def get_cpu_utilization(request):
    if platform.system() == "Windows":
        # cpu_cmd = "wmic cpu get loadpercentage /format:value"
        # cpu_percent = float(re.search(r'\d+',k.check_output(cpu_cmd).decode()).group())
        cpu_cmd = k.run(['wmic', 'cpu', 'get', 'loadpercentage'],capture_output=True)
        cpu_percent = float(re.search(r'\d+',cpu_cmd.stdout.decode()).group())
        ram_percent = psutil.virtual_memory().percent
        # print("Current CPU Usage is", cpu_percent, "%")
        # print("Current RAM Usage is", psutil.virtual_memory().percent, "%")
        return Response({'cpu_percent':cpu_percent, 'ram_percent':ram_percent})
    elif platform.system() == "Linux":
        cpu_cmd = "mpstat | awk '$3 ~ /CPU/ { for(i=1;i<=NF;i++) { if ($i ~ /%idle/) field=i } } $3 ~ /all/ { print 100 - $field }'"
        cpu_percent = str(os.popen(cpu_cmd).read())[:-2]
        ram_percent = psutil.virtual_memory().percent
        # print("Current CPU Usage is "+cpu_percent_linux+" %")
        # print("Current RAM Usage is "+ psutil.virtual_memory().percent +" %")
        return Response({'cpu_percent':cpu_percent, 'ram_percent':ram_percent})

def sendmail(request):
    check = send_mail('CPU Memory Low Alert', 'CPU usage more than 50%.', 'mail@example.com', ['vinodh17k@gmail.com'], fail_silently=False)
    if check :
        return HttpResponse('done')
    else:
        return HttpResponse('not done')

def add_or_view_subscriber(request):
   """ List all subscribers , or create a new subscriber. """

   if request.method == 'GET':
       subscribers = Subscriber.objects.all()
       return render(request,'subscriber_list.html',context={'subscribers':subscribers})

   elif request.method == 'POST':
       data = JSONParser().parse(request)
       serializer = SubscriberSerializer(data=data)
       if serializer.is_valid():
           serializer.save()


