from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def root(request):
    return HttpResponse("Go to the /phone or /computer routes please")

def index(request):
    return HttpResponse("This is the computerApp route!")