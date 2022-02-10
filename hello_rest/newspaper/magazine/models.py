from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.name



class Magazine(models.Model):
    name = models.CharField(max_length=100)
    number = models.SmallIntegerField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    content = models.TextField()
    slug = models.SlugField(blank=True, unique=True)
    created_date = models.DateField(auto_now_add=True, null=True)

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        return super().save( *args, **kwargs)

    def __str__(self) -> str:
        return self.name



class Author(models.Model):
    name = models.CharField(max_length=100)


    def get_author_full_name(self):
        return f"{self.name} hi"


    