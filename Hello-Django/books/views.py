from typing import Any, Dict, Reversible
from django.db import models
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView
from django.urls import reverse

from .models import Book, Comment
from .forms import CommnetForm


class BookListView(ListView):
    model = Book
    template_name = "books/index.html"
    context_object_name = "books"

class BookDetailView(DetailView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"
    slug_field = 'book_slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx["form"] = CommnetForm()
        ctx["comments"] = self.get_object().comments.all()
        return ctx


def add_comment(request, book_slug):
    if request.method == "POST":
        form = CommnetForm(request.POST)
        book = get_object_or_404(Book, book_slug=book_slug)
        if form.is_valid():
            # username = form.cleaned_data.get("username")
            # content = form.cleaned_data.get("content")
            # rate = form.cleaned_data.get("rate")
            # comment = Comment(username=username, content= content, rate=rate, book=book)
            form.save(book=book)
            return redirect(reverse("book_detail", kwargs={"slug": book_slug}))
        else:
            comments = book.comments.all()
            ctnx = {
                "comments": comments, 
                "book": book,
                "form": form
            }
            return render(request, "books/book_detail.html", ctnx)
            
