
# from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    context = {}
    context['hello'] = 'Hello World~'
    return render(request,'hello.html',context)

def login(request):
    context = {}
    context['login'] = 'login here'
    return render(request,'login.html',context)