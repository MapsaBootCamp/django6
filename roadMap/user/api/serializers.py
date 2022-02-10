from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

User = get_user_model()

# class ReadOnlyModelSerializer(serializers.ModelSerializer):
#     def get_fields(self, *args, **kwargs):
#         fields = super().get_fields(*args, **kwargs)
#         for field in fields:
#             fields[field].read_only = True
#         return fields


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(
        label=_("Email"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )