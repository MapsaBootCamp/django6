from django.urls import path

from .views import mentor_list, login, logout, register, SignUp, verify_code
from user.api.api_views import login_api

app_name = 'user'

urlpatterns = [
    path('mentors/', mentor_list, name="mentor_list"),
    path('account/login/', login, name="login"),
    path('account/register/', register, name="register"),
    path('account/signup/', SignUp.as_view(), name="sign_up"),
    path('account/logout/', logout, name="logout"),
    path('activation/', verify_code, name="activation"),
    path('api/login-ba-token-rest/', login_api)
]
