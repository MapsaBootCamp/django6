from django.contrib import admin
from django.urls import path, include
from django.urls.base import reverse
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="home"),
    path('user/', include("user.urls", namespace='users')),
    path('course/', include("courses.urls", namespace='courses')),
    path("", include("resume.urls", namespace='resume')),
    path("cart/", include("cart.urls", namespace='cart')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
