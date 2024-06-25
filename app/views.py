from django.http import HttpResponse
from django.shortcuts import render
# def home(request):
    # return HttpResponse("hiii django")
def home(request):
    return render(request,'home.html')