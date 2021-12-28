from django.urls import path

from .views import course_list, category_course, course_search, TestTemplateView, CourseList

app_name = "courses"

urlpatterns = [
    path("course-list", course_list, name="course_list"),
    path("course-search", course_search, name="course_search"),
    path("course-cat-list/<int:id>/", category_course, name="course_cat_list"),
    path("", TestTemplateView.as_view(), name="test"),
    path("course-list-by-cbv/", CourseList.as_view())
]

