from django.contrib import admin

from .models import CourseCategory, Course, Comment, CourseChapterMedia, CourseChapter



class CourseItemInline(admin.StackedInline):
    model = CourseChapterMedia

@admin.register(CourseChapter)
class CourseChapterInline(admin.ModelAdmin):
    inlines = [CourseItemInline]

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Comment)
