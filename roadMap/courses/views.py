from os import name
from typing import Any, Dict
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from user.views import login


from .models import Course, CourseCategory

def get_course_categories():
    return list(CourseCategory.objects.values())


@login_required(login_url="/user/account/login/")
def course_list(request):
    courses = list(Course.objects.values("category__title", "name", "price"))
    context =  {"course_data": courses, "name": "ashkan", "course_category": get_course_categories()}
    return render(request, "courses/index.html", context)


class CourseList(LoginRequiredMixin, ListView):
    model = Course
    # queryset = Course.objects.all()
    paginate_by = 10
    context_object_name = "courses"
    template_name = "courses/index.html"
    login_url = "/user/account/login/"

    def get_queryset(self):
        qs =  super().get_queryset()
        print(qs)
        return qs

def category_course(request, id):
    course = list(Course.objects.filter(category_id=id))
    context =  {"courses": course ,"course_category": get_course_categories()}
    return render(request, "courses/course_cat_detail.html", context)


def course_search(request):
    search_value = request.GET.get("q", "")
    qs = Course.objects.filter(name__icontains=search_value)
    ctx = {"courses": qs ,"course_category": get_course_categories()}
    return render(request, "courses/course_cat_detail.html", ctx)



class TestTemplateView(TemplateView):
    template_name = "courses/test.html"
    # extra_context = {"name": "asghar"}

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context  = super().get_context_data(**kwargs)
        context["name"] = "asghar"
        return context

