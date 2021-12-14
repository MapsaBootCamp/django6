from django.contrib import admin

from .models import CourseCategory, Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    pass

