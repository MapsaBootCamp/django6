from django.contrib import admin

from .models import CourseCategory, Course, Comment


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request)
    pass


@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Comment)


class CourseAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        if request.user.is_superuser:
            return super(CourseAdmin, self).get_queryset(request)
        else:
            request.user.has_perm('user.edit_cours')
            self.fieldsets = ('enformaition ', {'fields': ('email', 'description', 'price')}),
           
            courses = Course.objects.filter(mentor__id=request.user.id)
            return courses