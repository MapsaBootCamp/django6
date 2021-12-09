from django.contrib import admin
from django.db import models

from .models import Todo

admin.site.register(Todo)