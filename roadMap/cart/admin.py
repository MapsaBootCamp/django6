from django.contrib import admin

from .models import Cart, CartItem


class CartItemInline(admin.StackedInline):
    model = CartItem


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]

