from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=255)
    due_date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title