from django.urls import path

from .views import mentor_list, login, logout, register

app_name = 'user'

urlpatterns = [
    path('mentors/', mentor_list, name="mentor_list"),
    path('account/login/', login, name="login"),
    path('account/register/', register, name="register"),
    path('account/logout/', logout, name="logout"),
]
