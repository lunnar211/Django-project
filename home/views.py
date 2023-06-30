from django.shortcuts import render,HttpResponse
from home.models import Contact

# Create your views here.
def index(request):
    context ={
        "variable":"Dipesh is hacker"
    }
    return render(request,'index.html',context)
    # return HttpResponse("this is homepage")
def services(request):
    return render(request,'services.html')
    # return HttpResponse("this is aboutpage")
def login(request):
    return render(request,'login.html')
    # return HttpResponse("this is services page")
def signup(request):
    return render(request,'signup.html')
    # return HttpResponse("this is contact page")

def about(request):
    return render(request,'about.html')
def base(request):
    return render(request,'base.html')
def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('messsage')
        contact=contact(name=name,email=email,phone=phone,message=message)
        contact.save()
    return render(request,'contact.html')


def transaction(request):
    return render(request,'transaction.html')
def home(request):
    return render(request,'index.html')
def accounts(request):
    return render(request,'accounts.html')