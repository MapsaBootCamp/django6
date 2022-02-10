from django.urls import path

from .views import (course_list, category_course, course_search,
                    TestTemplateView, CourseList, CourseDetail, add_comment, publish_video, send_mail_test)

from courses.api.api_views import CourseListView


app_name = "courses"

urlpatterns = [
    path("course-list", course_list, name="course_list"),
    path("course-search", course_search, name="course_search"),
    path("course-cat-list/<int:id>/", category_course, name="course_cat_list"),
    path("", TestTemplateView.as_view(), name="test"),
    path("course-list-by-cbv/", CourseList.as_view()),
    path("course-detail/<int:course_id>", CourseDetail.as_view()),
    path("add-comment/<int:course_id>", add_comment, name="add_comment"),
    path("publish-course-content/<int:course_media_id>", publish_video, name="publish_video"),
    path("api/course-list/", CourseListView.as_view()),
    path("test-celery", send_mail_test),

]
