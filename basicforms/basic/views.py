from django.shortcuts import render
from basic import forms 
# Create your views here.

def index(request):
    return render(request,'basicapp/index.html')


def form_view(request):
    form =forms.FormName()
    return render(request,'basicapp/forms.html',{
        'form':form
    })