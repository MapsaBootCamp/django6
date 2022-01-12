from django.urls import path

from .views import BookListView, BookDetailView, add_comment

urlpatterns = [
    path('book-list/', BookListView.as_view(), name="book_list"),
    path('book-detail/<str:slug>', BookDetailView.as_view(), name="book_detail"),
    path('add-comment/<str:book_slug>', add_comment, name="add_comment"),
]


