from django.http import JsonResponse
from django.contrib.auth.models import User

from app.models import Profile


def token_validation(f):
    """check if token is valid"""
    def check(request, *args, **kwargs):
        token = request.META.get("HTTP_AUTHORIZATION")
        try:
            user = Profile.objects.get(token=token).user
        except:
            user = None
        if not user:
            return JsonResponse({
                "status": "Failed",
                "error": "Token invalid"
            }, status=401)

        return f(request, user, *args, **kwargs)

    return check
