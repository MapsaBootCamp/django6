from django.shortcuts import get_object_or_404, render


from .models import Course, CourseCategory

def get_course_categories():
    return list(CourseCategory.objects.values())


def course_list(request):
    courses = list(Course.objects.values("category__title", "name", "price"))
    context =  {"course_data": courses, "name": "ashkan", "course_category": get_course_categories()}
    return render(request, "courses/index.html", context)


def category_course(request, id):
    course = list(Course.objects.filter(category_id=id))
    context =  {"courses": course ,"course_category": get_course_categories()}
    return render(request, "courses/course_cat_detail.html", context)


def course_search(request):
    search_value = request.GET.get("q", "")
    qs = Course.objects.filter(name__icontains=search_value)
    ctx = {"courses": qs ,"course_category": get_course_categories()}
    return render(request, "courses/course_cat_detail.html", ctx)
