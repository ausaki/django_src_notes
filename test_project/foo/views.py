from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.

def abc(request):
    reverse('abc')
    return HttpResponse('hello world')