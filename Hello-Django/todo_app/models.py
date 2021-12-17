from django.db import models
from django.db.models.deletion import SET_NULL


class User(models.Model):
    username = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.username


class Profile(models.Model):
    img = models.ImageField(upload_to="users/", null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class Todo(models.Model):
    title = models.CharField(max_length=255)
    due_date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ManyToManyField(Category)
    
    def __str__(self) -> str:
        return self.title


class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication, through="PublicationArticle")

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline


class PublicationArticle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    publications = models.ForeignKey(Publication, on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField()



    class Meta:
        db_table = "publicatin_article"