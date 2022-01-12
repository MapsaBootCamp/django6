from django.urls import path

from .views import add_to_cart, show_cart

app_name = "cart"

urlpatterns = [
    path("add-cart/", add_to_cart, name="add-cart"),
    path("show-cart/", show_cart, name="show-cart"),
]
