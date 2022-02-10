from os import name
from typing import Any, Dict
from django.db import models
from django.db.models.query import QuerySet
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.contrib.auth.decorators import permission_required

from user.views import User, login


from .models import Course, CourseCategory, CourseChapterMedia
from .forms import CommentForm
from .tasks import send_email_task

def send_mail_test(request):
    send_email_task.delay("ashkan", "khab darim")
    return HttpResponse("send mail by celery")


def get_course_categories():
    return list(CourseCategory.objects.values())


@login_required(login_url="/user/account/login/")
def course_list(request):
    courses = list(Course.objects.values("category__title", "name", "price"))
    context = {"course_data": courses, "name": "ashkan",
               "course_category": get_course_categories()}
    return render(request, "courses/index.html", context)


class CourseList(LoginRequiredMixin, ListView):
    model = Course
    # queryset = Course.objects.all()
    paginate_by = 10
    context_object_name = "courses"
    template_name = "courses/index.html"
    login_url = "/user/account/login/"

    def get_queryset(self):
        qs = super().get_queryset()
        print(qs)
        return qs


def category_course(request, id):
    course = list(Course.objects.filter(category_id=id))
    context = {"courses": course, "course_category": get_course_categories()}
    return render(request, "courses/course_cat_detail.html", context)


def course_search(request):
    search_value = request.GET.get("q", "")
    qs = Course.objects.filter(name__icontains=search_value)
    ctx = {"courses": qs, "course_category": get_course_categories()}
    return render(request, "courses/course_cat_detail.html", ctx)


class CourseDetail(DetailView):
    model = Course
    template_name = "courses/course_detail.html"
    context_object_name = "course"
    pk_url_kwarg = "course_id"

    def get_context_data(self, *args, **kwargs):
        ctnx = super().get_context_data(*args, **kwargs)
        ctnx["comments"] = self.get_object().comments.all()
        ctnx["form"] = CommentForm()
        return ctnx


class TestTemplateView(TemplateView):
    template_name = "courses/test.html"
    # extra_context = {"name": "asghar"}

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["name"] = "asghar"
        return context


@login_required(login_url="/user/account/login/")
def add_comment(request, course_id):
    if request.method == "POST":
        course = get_object_or_404(Course, id=course_id)
        if course.students.filter(user=request.user.pk).exist():
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.course = course
                comment.save()
            return redirect("courses:course_detail")
        else:
            return redirect("courses:course_detail")


@permission_required(["courses.can_publish"], login_url="/user/account/login/", raise_exception=True)
def publish_video(request, course_media_id):
    course_media = get_object_or_404(CourseChapterMedia, id=course_media_id)
    course_media.is_publish = True
    course_media.save()
    # print(request.user.has_perm("courses.can_publish"), request.user.email)
    return JsonResponse({
        "status" : "Done!"
    })
