from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def lyrics(request):
    return render(request,"lyrics/home.html",{})