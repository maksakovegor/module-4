from django.http import HttpRespounse
from django.shortcuts import render

def index(request):
    return HttpRespounse('True')