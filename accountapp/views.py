from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def go_home(request):
    return HttpResponse('you may go home')