from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def login(request):
    context = {}
    context['login'] = 'login here'
    return render(request,'login.html',context)

def miniLogin(request):
    pass