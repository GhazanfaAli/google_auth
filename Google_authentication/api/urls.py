from django.urls import include, path, re_path
from api.views import GoogleLogin, GoogleLoginCallback

urlpatterns = [
    #path("api/v1/auth/google/", GoogleLogin.as_view(), name="google_login"),
    #path("api/v1/auth/google/callback/", GoogleLoginCallback.as_view(), name="google_login_callback"),
    path("accounts/google/login/", GoogleLogin.as_view(), name="google_login"),
    path("accounts/google/login/callback/", GoogleLoginCallback.as_view(), name="google_callback"),

]