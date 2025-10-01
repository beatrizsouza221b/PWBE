from django.shortcuts import render
from django.http import HttpResponse

def saudacao(request):
    return HttpResponse("Olá! Bem-vindo à biblioteca!")
# Create your views here.
