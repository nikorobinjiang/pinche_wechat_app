from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from django.http import HttpResponse

def login(request):
    context = {}
    context['login'] = 'login here'
    return render(request,'login.html',context)

def getTripList(request):
    return HttpResponse()