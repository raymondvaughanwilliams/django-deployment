from django.shortcuts import render
from form.forms import NewUser
# Create your views here.

def index(request):
    return render(request,'formss/index.html')


def form_view(request):
    form =forms.FormName()

    if request.method == "POST":
        form =forms.FormName(request.POST)

        if form.is_valid():
            print("working")
            print(form.cleaned_data['name'])
        
    return render(request,'formss/form.html',{'form':form})


def signup_view(request):
    form = NewUser()

    if request.method =='POST':
        form =NewUser(request.POST)

        if form.is_valid():
            form.save(commit =True)
            return index(request)

        else:
            print("Error")
    return render(request,'formss/signup.html',{'form':form})