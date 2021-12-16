from django.urls import path

from .views import mentor_list

app_name = 'user'

urlpatterns = [
    path('mentors/<int:id>', mentor_list, name="mentor_list")
]
