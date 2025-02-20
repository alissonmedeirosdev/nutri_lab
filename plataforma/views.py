from django.shortcuts import render
from django.http import HttpResponse

def paciente(request):
    return HttpResponse('Testando!')
