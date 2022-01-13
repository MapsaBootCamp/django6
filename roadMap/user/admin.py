from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from courses.models import Course

from .models import Profile, Mentor, User
from .forms import CustomUserChangeForm, CustomUserCreationForm

User = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        ('اطلاعات اصلی', {'fields': ('email', 'password', 'first_name')}),
        ('Permissions', {
         'fields': ('is_staff', 'is_active', 'user_permissions')}),
    )
    add_fieldsets = (
        ("اطلاعات کاربری", {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2',)
        },
        ), (
            "سطح دسترسی", {
                'fields': ('is_staff', 'is_active', 'user_permissions')
            }

        )
    )
    search_fields = ('is_staff',)
    ordering = ('email',)


   
         
         
        # if request.user.is_superuser:
        #     return qs
        # return qs.filter(Mentor=request.user)



    # qs.filter()

class CustomMentorAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Mentor
    list_display = ('email', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        ('اطلاعات اصلی', {'fields': ('email', 'password', 'first_name')}),
        ('Permissions', {
         'fields': ('is_staff', 'is_active', 'user_permissions')}),
    )
    add_fieldsets = (
        ("اطلاعات کاربری", {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2',)
        },
        ), (
            "سطح دسترسی", {
                'fields': ('is_staff', 'is_active', 'user_permissions')
            }

        )
    )
    search_fields = ('is_staff',)
    ordering = ('email',)
   


admin.site.register(Profile)
admin.site.register(Mentor,CustomMentorAdmin)
admin.site.register(User, CustomUserAdmin)
