from django.contrib import admin
from django.urls import path, include
from django.urls.base import reverse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include("user.urls", namespace='users'))
]

