import imp
from itertools import permutations
from lib2to3.pgen2.grammar import opmap
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


def add_permission(model,code_name,name):

    content_type=ContentType.objects.get_for_model(model)
    
    if Permission.objects.filter(code_name=code_name):
        raise Exception('permission already exist')
    else:
        permission=Permission.objects.create(
            codename='editcourse',
            name='edit_cours',
            content_type=content_type,
        )


