from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db.models.manager import Manager

User = get_user_model()

class Profile(User):
    phone_number = models.CharField(max_length=11, verbose_name="شماره تلفن")
    img = models.ImageField(upload_to="profiles/", null=True, blank=True)
    
    class Meta:
        verbose_name = "Profile"


    def __str__(self) -> str:
        return self.username

class Mentor(Profile):
    
    SKILL_CHOICES = [
        ('C', 'Computer Engineering'),
        ('E', 'Econimic'),
        ('P', 'Philosophy'),
    ]

    major = models.CharField(max_length=1, choices=SKILL_CHOICES)

    class Meta:
        verbose_name = "Mentor"


    def __str__(self) -> str:
        return self.username