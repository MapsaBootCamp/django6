from django.contrib import admin

from .models import Author, Book, Publisher, Store

class BookAdmin(admin.ModelAdmin):
    exclude = ("book_slug",)


admin.site.register(Author)
admin.site.register(Book, BookAdmin)
admin.site.register(Publisher)
admin.site.register(Store)