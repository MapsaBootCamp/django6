from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

def email_validator(value):
    if "mapsa" not in value:
        raise ValidationError("mapsa not in email", code="mapsa")
    return value


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(validators=[email_validator])
    class Meta:
        model = User
        fields = ['email',
                  'password1', 'password2']
        labels = {
            "email": "ایمیل",
            "password1": "رمز عبور",
            "password2": "تکرار رمز عبور",

        }

        help_texts = {
            "email": "ایمیل خود را به درستی وارد کنید",
            "password1": "باید بیش از ۸ کارکتر باشد"
        }
        error_messages = {
            'email': {
                'mapsa': "the shalgham you need mapsa.",
            },
        }

    # def clean(self):
    #     data = self.cleaned_data.get("email")
    #     if "mapsa" not in data:
    #         raise ValidationError("hhhh", code="mapsa")
    #     return data

    def save(self, commit=True):
        '''
        override user create form to create profile after register!
        '''
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = False
        user.save()

        # try:
        #     # if commit:
        #     user.save()
        #     Profile.objects.create(user=user, phone=self.cleaned_data["phone"])

        # except Exception as e:
        #     user.delete()
        #     raise ValueError(f"cant create profile object! reason: {e}")

        return user


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'first_name')


class CodeValidationForm(forms.Form):
    email = forms.EmailField(widget=forms.HiddenInput())
    code = forms.CharField(max_length=6)