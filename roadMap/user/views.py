from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, logout as _logout, login as _login


from .models import Mentor, Profile


User = get_user_model()

def mentor_list(request):
    qs = list(Mentor.objects.values("major", "profile_ptr__phone_number"))
    # print(reverse("users:mentor_list", kwargs={"id": id}))
    return JsonResponse({"data": qs})


@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "GET":
        return render(request, "registration/login.html")
    else:
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            _login(request, user)
            return redirect('home')
        else:
            return redirect('users:login')


def logout(request):
    _logout(request)
    return redirect('home')

@require_http_methods(["GET", "POST"])
def register(request):
    if request.method == "GET":
        return render(request, "registration/register.html")
    else:
        username = request.POST.get("username", "")
        phone = request.POST.get("phone", "")
        if not username:
            return render(request, "registration/register.html", {"error": "shlgham username ra vared kon"})
        password1 = request.POST.get("password1", "")
        password2 = request.POST.get("password2", "")
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return render(request, "registration/register.html", {"error": "shlgham chenin useri darim"})
            else:
                try:
                    user = Profile(username=username, phone_number=phone)
                    user.set_password(password1)
                    user.save()
                    _login(request, user)
                    return redirect('home')
                except:
                    return render(request, "registration/register.html", {"error": "dobare talash kon"})

        else:
            return render(request, "registration/register.html", {"error": "shlgham pass1 va pass2 yeki bezan"})




