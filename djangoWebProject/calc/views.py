from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# accept the request
def home(request):
    return HttpResponse("Hello World")

def home1(request):
    return render(request,'home.html',{'name' :'Kaushi'})

def homepost(request):
    return render(request,'home-post.html',{'name' :'Kaushi'})

def add(request):
    val1 = request.GET['num1']
    val2 = request.GET['num2']

    res = int(val1) + int(val2)
    return render(request,'result.html',{'result' :res})
def addb(request):
    val1 = request.POST['num1']
    val2 = request.POST['num2']

    res = int(val1) + int(val2)
    return render(request,'result.html',{'result' :res})