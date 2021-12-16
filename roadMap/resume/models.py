from django.db import models

from user.models import Profile

class Resume(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    education = models.JSONField(null=True)
    work_exprience = models.JSONField(null=True)
    description = models.TextField()


    def __str__(self) -> str:
        return self.user.username