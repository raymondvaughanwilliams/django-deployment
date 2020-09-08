
from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User 
# Create your views here.
def index(request):
    return HttpResponse("My Second App")


def help(request):
    context ={
        'inserted':'inserted'
    }
    return render(request,'index.html',context)


def users(request):
    user_list =User.objects.order_by('first_name')
    user_details = {'users':user_list}
    return render(request,'users.html',context=user_details)