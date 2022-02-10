from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import News, Comment
from .serializers import CommentSerializer, NewsListSerializer, NewsDetailSerializer


# class NewsList(APIView):
    
#     def get(self, request):
#         queryset = News.objects.all()
#         serilizer = NewsListSerializer(queryset, context={"request": request}, many=True)
#         print(serilizer.data)
#         return Response(serilizer.data)

#     def post(self, request):
#         serilizer = NewsListSerializer(data=request.data)
#         if serilizer.is_valid():
#             serilizer.save()
#             return Response(serilizer.data, status=status.HTTP_201_CREATED)
#         return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

class NewsListView(ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializer


class NewsDetailView(RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer
    lookup_field = "slug"


class CommentView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer