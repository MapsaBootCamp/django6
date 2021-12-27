from django import template
from courses.models import CourseCategory
from django.utils.safestring import mark_safe
from django.urls import reverse

register = template.Library()

@register.simple_tag
def get_course_cat():
    categories = CourseCategory.objects.all()
    result = ""
    for category in categories:
        result += f'<li><a href=' + reverse('courses:course_cat_list', kwargs={"id": category.id}) + f">{category.title}</a> </li>"
    return mark_safe(result)

