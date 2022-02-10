from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login as _login, authenticate
from django.conf import settings

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .serializers import LoginSerializer, User

@api_view(["POST"])
def login_api(request):
    serializer = LoginSerializer(data=request.data)
    result = {}
    if serializer.is_valid():
        email=serializer.validated_data["email"]
        password=serializer.validated_data["password"]
        user = authenticate(email=email, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            if settings.ROADMAP_TOKEN_VALIDATION_DAY and isinstance(settings.ROADMAP_TOKEN_VALIDATION_DAY, int):
                now = timezone.now()
                differnce = now - token.created
                if differnce.days > settings.ROADMAP_TOKEN_VALIDATION_DAY:
                    token.delete()
                    token = Token.objects.create(user=user)

            result["successful"] = True
            result["error"] = False
            result["data"] = {"status": "be khubi va khoshi login shod", "token": token.key}
            return Response(result)
        else:
            result["successful"] = False
            result["error"] = True
            result["error_message"] = "username ya pass eshtebahe"
            return Response(result, status=status.HTTP_404_NOT_FOUND)

    else:
        result["successful"] = False
        result["error"] = True
        result["error_message"] = serializer.errors
        return Response(result, status=status.HTTP_404_NOT_FOUND)


