from django.contrib.auth.models import  Permission
from django.contrib.contenttypes.models import ContentType

content_type = ContentType.objects.get(app_label='user', model='mentor')

mentor_per = Permission.objects.create(codename='Mentor_access',
                                       name='Can change his courses',
                                       content_type=content_type) 