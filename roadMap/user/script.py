from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from user.models import Mentor



content_type = ContentType.objects.get_for_model(Mentor)

mentor_permission = Permission.objects.create(codename ='editcourse',
										      name ='edit_cours',
											  content_type = content_type)


