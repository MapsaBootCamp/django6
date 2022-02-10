from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from courses.models import Course
from .serializers import CourseModelSerializer


class CourseListView(ListAPIView):

    permission_classes = [IsAuthenticated]
    queryset = Course.objects.all()
    serializer_class = CourseModelSerializer