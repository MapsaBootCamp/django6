from django.urls import path

from .views import NewsDetailView, NewsListView, CommentView


urlpatterns = [
    path('news-list', NewsListView.as_view(), name="news_list"),
    path('news-detail/<str:slug>', NewsDetailView.as_view(), name="news_detail"),
    path('news-comment', CommentView.as_view(), name="comment_news"),
]