from django.contrib import admin
from django.db import models

from .models import Todo, User, Profile, Category

admin.site.register(Todo)
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Category)