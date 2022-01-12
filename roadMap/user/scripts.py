from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from user.models import Mentor

new_group, created = Group.objects.get_or_create(name ='groh_mentorha')

ct = ContentType.objects.get_for_model(Mentor)

permission = Permission.objects.create(codename ='edit_course',
										name ='can mentor edit his/her own courses',
												content_type = ct)
new_group.permissions.add(permission)
