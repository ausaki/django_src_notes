from os import name
from django.urls import include, path
from .views import abc

# app_name = 'foo'

urlpatterns = [
    path('abc', abc, name='abc')
]