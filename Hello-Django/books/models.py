from django.db import models, connection
from django.utils.text import slugify


class AuthorManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(age__lt = 20)

    def truncate(self):
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE "{self.model._meta.db_table}" CASCADE')
     


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    objects = models.Manager()
    javan = AuthorManager()
    

    def __str__(self) -> str:
        return self.name

    @classmethod
    def truncate(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE "{cls._meta.db_table}" CASCADE')


class Publisher(models.Model):
    name = models.CharField(max_length=300)

class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, related_name="books", on_delete=models.CASCADE)
    pubdate = models.DateField()
    book_slug = models.SlugField(blank=True, null=True, unique=True)

    def __str__(self) -> str:
        return self.book_slug

    def save(self, *args, **kwargs):
        if not self.book_slug:
            self.book_slug = slugify(f"{self.name} {self.publisher.name}", allow_unicode=True)
        return super().save(*args, **kwargs)

class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)

class Comment(models.Model):
    username = models.CharField(max_length=100)
    content = models.TextField()
    rate = models.FloatField()
    book = models.ForeignKey(Book, related_name="comments", on_delete=models.CASCADE)