from cgitb import lookup
import imp
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from magazine.serializers import AuthorSerializer, MagazineListSerializer, MagazineDetailSerializer
from magazine.models import Author, Magazine


class MagazineViewSet(ReadOnlyModelViewSet):
    queryset = Magazine.objects.all()
    lookup_field = "slug"

    serializers = {
        "list": MagazineListSerializer,
        "retrieve": MagazineDetailSerializer,
    }


    def get_serializer_class(self):
        return self.serializers.get(self.action)


class AuthorList(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]