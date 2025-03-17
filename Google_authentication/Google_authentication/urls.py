from django.urls import path, include
from django.contrib import admin
from api.views import home  # Import the home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('api.urls')),
    path('accounts/', include('allauth.urls')),
    path('', home, name='home'),  # Map root URL to the home view
]