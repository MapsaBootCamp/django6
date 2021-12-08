from django.contrib import admin
from django.http.response import HttpResponse
from django.urls import path, include, re_path

def hello(request):
    return HttpResponse("salam")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('salam/', include("todo_app.urls"), name="todo"),
    path('', hello)
]
