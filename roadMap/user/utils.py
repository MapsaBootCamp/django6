from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


content_type = ContentType.objects.get(app_label='user', model='mentor')
permission = Permission.objects.create(
    codename='can_edit_course',
    name='Can Edit Own Course',
    content_type=content_type,
)
