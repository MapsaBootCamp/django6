from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db.models.manager import Manager
from django.contrib.auth.models import AbstractUser, UserManager, BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        db_table = 'auth_user'


class Profile(User):
    phone_number = models.CharField(max_length=11, verbose_name="phone number")
    img = models.ImageField(upload_to="profiles/", null=True, blank=True)

    class Meta:
        verbose_name = "Profile"

    def __str__(self) -> str:
        return self.email


class Mentor(Profile):

    SKILL_CHOICES = [
        ('C', 'Computer Engineering'),
        ('E', 'Econimic'),
        ('P', 'Philosophy'),
    ]

    major = models.CharField(max_length=1, choices=SKILL_CHOICES)

    class Meta:
        verbose_name = "Mentor"
        permissions = [
            ('edit_course', 'can mentor edit his/her own courses',)
        ]

    def __str__(self) -> str:
        return self.email
