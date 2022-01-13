from django.contrib import admin

from .models import CourseCategory, Course, Comment


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    def get_queryset(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().get_queryset(request)
        elif request.user.has_perm('user.edit_course'):
            self.fieldsets = (
                ('اطلاعات منتور', {
                    'classes': ('wide',),
                    'fields': ('name', 'category', 'img', 'price', 'description')
                }),
            )
            mentor_courses = Course.objects.filter(mentor__id=request.user.id)
            return mentor_courses



@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Comment)
