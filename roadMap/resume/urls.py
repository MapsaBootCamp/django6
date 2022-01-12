from django.urls import path

from .views import ResumeView

app_name = "resume"

urlpatterns = [
    path("resume/", ResumeView.as_view(), name="show_resume"),

]

