from django.contrib import admin
from django.urls import path, include
from django.urls.base import reverse
from django.conf import settings
from django.conf.urls.static import static


from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="home"),
    path('user/', include("user.urls", namespace='users')),
    path('course/', include("courses.urls", namespace='courses')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
