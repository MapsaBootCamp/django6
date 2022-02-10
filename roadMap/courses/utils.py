from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from courses.models import CourseChapterMedia

def add_custom_permission_to_model(model, code_name, name):

    content_type = ContentType.objects.get_for_model(model)
    
    if  Permission.objects.filter(codename=code_name).exists():
        raise Exception("permission already exist")
    else:

        permission = Permission.objects.create(
        codename=code_name,
        name=name,
        content_type=content_type,
        )
        return permission


