from django.conf import settings
from django.db import models
from django.conf import settings
from django.utils.text import slugify


class News(models.Model):
    author = models.ManyToManyField(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    slug = models.SlugField(null=True, unique=True, blank=True)

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    news = models.ForeignKey(News, related_name="comments", on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
