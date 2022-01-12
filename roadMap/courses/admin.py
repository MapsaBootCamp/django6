from django.contrib import admin

from .models import CourseCategory, Course, Comment



@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Comment)


@admin.register(Course)
class Adminshow(admin.ModelAdmin):

    def get_queryset(self, request) :
 
        
        if request.user.is_superuser:
            query_set=Course.objects.all()
            return query_set

        if request.user.has_perm("courses.Mentor_can_see"):
        
            query_set=Course.objects.filter(mentor__id=request.user.id)
            print(query_set,"asddad")
            return query_set

