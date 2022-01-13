from ast import Raise
import imp
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


def add_permission_to_model(model,code_name,name):
    content_type=ContentType.objects.get_for_model(model)
    if Permission.objects.filter(codename=code_name).exists():
         raise Exception("permission already exists")
    else:
         Permission.objects.create(content_type=content_type,codename=code_name,name=name)
         return Permission





