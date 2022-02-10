import random

from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, logout as _logout, login as _login
from django.views import View
from django.core.cache import cache

from user.forms import CustomUserCreationForm, CodeValidationForm


from .models import Mentor, Profile


User = get_user_model()

def mentor_list(request):
    qs = list(Mentor.objects.values("major", "profile_ptr__phone_number"))
    # print(reverse("users:mentor_list", kwargs={"id": id}))
    return JsonResponse({"data": qs})


@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "GET":
        ctx = {}
        next = request.GET.get("next", "")
        if next:
            ctx["next"] = next
        return render(request, "registration/login.html", ctx)
    else:
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            _login(request, user)
            next = request.GET.get("next", "")
            if next:
                return redirect(next)
            return redirect('home')
        else:
            return redirect('users:login')


def logout(request):
    _logout(request)
    return redirect('home')

class SignUp(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("home")
        form = CustomUserCreationForm()
        return render(request, "registration/signup.html", {"form": form})


    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            rand_key = random.randint(10**5, 10**6 -1)
            print(rand_key)
            cache.set(email, str(rand_key), timeout=120)
            code_validation_form = CodeValidationForm({"email": email})
            return render(request, "registration/verify.html", {"form": code_validation_form})
        return render(request, "registration/signup.html", {"form": form})




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


@require_http_methods(["POST"])
def verify_code(request):
    form = CodeValidationForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data.get("email")
        code = form.cleaned_data.get("code")
        code_in_cache = cache.get(email)
        if code_in_cache:
            if code == code_in_cache:
                user = get_object_or_404(User, email=email)
                user.is_active = True
                user.save()
                _login(request, user)
                return redirect("home")
            else:
                return render(request, "registration/verify.html", {"form": form})
        else:
            rand_key = random.randint(10**5, 10**6 -1)
            print(rand_key)
            cache.set(email, str(rand_key), timeout=120)
            form = CodeValidationForm({"email": email})
            return render(request, "registration/verify.html", {"form": form})
            
        
