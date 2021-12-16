from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse

from .models import Mentor


def mentor_list(request, id):
    qs = list(Mentor.objects.values("major", "profile_ptr__phone_number"))
    # print(reverse("users:mentor_list", kwargs={"id": id}))
    return JsonResponse({"data": qs})