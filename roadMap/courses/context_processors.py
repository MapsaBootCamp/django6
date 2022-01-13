from courses.models import CourseCategory

def get_course_cat(request):
    qs = CourseCategory.objects.all()
    return {"course_cat_from_processor": qs}