from django.http.response import HttpResponse
from django.shortcuts import render

def salam(request):
    return HttpResponse("salam aleikom")
    