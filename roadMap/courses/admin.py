from django.contrib import admin

from .models import CourseCategory, Course, Comment


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
     def get_queryset(self, request):
        qs=super().get_queryset(request)
        if request.user.has_perm("user.view_courses"):
            qs=Course.objects.filter(mentor__id=request.user.id)
        return qs



@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Comment)



