from django import forms
from django.db import models
from django.core.exceptions import ValidationError
from django.forms import fields

from .models import Book, Comment  


# class BookForm(forms.Form):
#     name = forms.CharField(max_length=300)
#     pages = forms.IntegerField()
#     price = forms.DecimalField(max_digits=10, decimal_places=2)



# class CommnetForm(forms.Form):
#     username = forms.CharField(max_length=100)
#     content = forms.CharField(widget=forms.Textarea)
#     rate = forms.FloatField()


#     def clean_username(self):
#         data = self.cleaned_data["username"]
#         if "mapsa" not in data:
#             raise ValidationError("mapsa bayad dar form shoma bashad!")
#         return data



class CommnetForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = ("username", "content", "rate")
        exclude = ("book",)
    
    def clean_username(self):
        data = self.cleaned_data["username"]
        if "mapsa" not in data:
            raise ValidationError("mapsa bayad dar form shoma bashad!")
        return data

    def save(self, *args, **kwargs):
        book = kwargs.pop("book")
        commit = kwargs.get("commit", True)
        self.instance.book = book
        return super().save(commit=commit)