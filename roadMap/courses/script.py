from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from courses.models import Course

content_type = ContentType.objects.get_for_model(Course)

permission = Permission.objects.create(
    codename='Mentor_can_see',
    name='Mentor can see his courses',
    content_type=content_type,
)