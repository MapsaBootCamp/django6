from rest_framework import serializers

from courses.models import Course

class CourseModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ["name", "mentor"]