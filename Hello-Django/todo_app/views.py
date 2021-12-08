from django.http.response import HttpResponse
from django.shortcuts import render

from .models import Todo


def todo_list(request):
    Todo.objects.all()