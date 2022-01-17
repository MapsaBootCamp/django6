from django.urls import path

from .views import (course_list, category_course, course_search,
                    TestTemplateView, CourseList, CourseDetail, add_comment)

app_name = "courses"

urlpatterns = [
    path("course-list", course_list, name="course_list"),
    path("course-search", course_search, name="course_search"),
    path("course-cat-list/<int:id>/", category_course, name="course_cat_list"),
    path("", TestTemplateView.as_view(), name="test"),
    path("course-list-by-cbv/", CourseList.as_view()),
    path("course-detail/<int:course_id>", CourseDetail.as_view()),
    path("add-comment/<int:course_id>", add_comment, name="add_comment"),
    # path("change-detail/", change_detail, name="change_detail"),

]
