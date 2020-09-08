from django.shortcuts import render
from django.http import HttpResponse
from baako.models import Topic,Webpage,AccessRecord
# Create your views here.


def index(request):
    webpages_list=AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    my_dict= {
        'insert_me':'From viewss'
    }
    return render(request,'baako/index.html',date_dict)


def jitsi(request):
    
    return render(request,'baako/jitsi.html')