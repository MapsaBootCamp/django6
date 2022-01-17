from courses.models import Course
from django.contrib.auth.models import Permission, PermissionManager
from django.contrib.contenttypes.models import ContentType


def vip_mentor(model , code_name ,name):

    content_type = ContentType.objects.get_for_model(model)

    if Permission.objects.filter(codename=code_name).exists():
        raise Exception("permission is already exist...!")
    else:
        permission = Permission.objects.create(
        codename='edit_self_course',
        name='can edit self course',
        content_type=content_type,)

        return permission