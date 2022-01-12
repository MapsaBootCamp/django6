from django.contrib import admin

from .models import CourseCategory, Course, Comment


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     return qs.filter(mentor=request.user)

     def get_queryset(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().get_queryset(request, *args, **kwargs)

        elif request.user.has_perm("user.Mentor_access"):
            qs_main = Course.objects.filter(mentor__id=request.user.id)
            return qs_main

@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Comment)
