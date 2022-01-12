from django.shortcuts import render
from django.http import JsonResponse

from .utils import add_to_cart_anonymous_user, show_cart_anonymous_user, clear_cart_anonymous_user

def add_to_cart(request):
    if not request.user.is_authenticated:
        add_to_cart_anonymous_user(request, request.GET.get("product"), request.GET.get("quantity"))
        return JsonResponse(
            {"status": "success"}
        )
    else:
        return JsonResponse(
            {"status": "failed"}
        )

def show_cart(request):
    if not request.user.is_authenticated:
        print(request.session.get("cart"))
        return JsonResponse(
            {"status": "success", "data": request.session.get("cart")}
        )
    else:
        return JsonResponse(
            {"status": "failed"}
        )