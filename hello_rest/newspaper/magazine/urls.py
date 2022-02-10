from django.urls import include, path

from rest_framework.routers import SimpleRouter, DefaultRouter

from magazine.views import AuthorList, MagazineViewSet


router = DefaultRouter()
router.register(r'magazine', MagazineViewSet, basename="magazine")
router.register(r'shalghan', MagazineViewSet, basename="shalgham")


urlpatterns = [
    path("authors/", AuthorList.as_view(), name="authors_list"),
] + router.urls