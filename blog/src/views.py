from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render(request,"home.html")
def loginpage(request):
    return render(request,"login.html")
def register(request):
    return render(request,"register.html")
def detail(request):
    return render(request,"detail.html")