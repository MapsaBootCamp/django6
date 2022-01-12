from django.contrib import admin

from .models import CourseCategory, Course, Comment


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        if request.user.is_superuser:
            return super(CourseAdmin, self).get_queryset(request)
        elif request.user.has_perm('user.can_edit_course'):
            self.fieldsets = (
                ('information', {
                    'classes': ('wide',),
                    'fields': ('name', 'category', 'img', 'price', 'description',)
                }),
            )
            courses = Course.objects.filter(mentor__id=request.user.id)
            return courses


@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Comment)
