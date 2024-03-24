from django.shortcuts import render   ## To render HTTP Pages
from django.http import HttpResponse  ## To Send HTTP Responses. 

# Create your views here.

def home_page(request):
    return render(request,'home.html')

def test(request):
    return HttpResponse("Test Message")

def rooms(request):
    return render(request,'rooms.html')