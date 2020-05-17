from django.shortcuts import render,HttpResponse
from .models import farmhouse_detail
# Create your views here.
def index(request):
    return render(request,'homepage.html')
def homepage(request):
    return render(request,'homepage.html')
def services_d(request):
    service = farmhouse_detail.objects.all()

    return render(request,'services.html',{'service':service})
def details(request):

    return render(request,'details.html')

def aboutus(request):
    return render(request,'about.html')