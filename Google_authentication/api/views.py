from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import os

from django.shortcuts import render

PORT = os.getenv("PORT", "9000")


def home(request):
    return render(request, 'index.html')

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = settings.GOOGLE_OAUTH_CALLBACK_URL  # This should now work
    
class GoogleLoginCallback(APIView):
    def get(self, request, *args, **kwargs):
        code = request.GET.get("code")
        if code is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # token_endpoint_url = urljoin(f"http://localhost:{PORT}", reverse("google_login"))
        # response = requests.post(url=token_endpoint_url, data={"code": code})
        # return Response(response.json(), status=status.HTTP_200_OK)
        token_endpoint_url = request.build_absolute_uri(reverse("google_login"))
        response = requests.post(url=token_endpoint_url, data={"code": code})
        return Response(response.json()), status=status.HTTP_200_OK