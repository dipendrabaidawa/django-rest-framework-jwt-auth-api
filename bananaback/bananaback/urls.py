from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from joboard.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # Path to obtain a new access and refresh token
    path('api/auth/signin', MyTokenObtainPairView.as_view(), name='login'),
    path('api/auth/signup', register, name='signup'),
    # Submit your refresh token to this path to obtain a new access token
    path('api/auth/refreshtoken', TokenRefreshView.as_view(), name='token_refresh'),
    path('', joboard, name='vueapp'),
    path('api/test/all', joboard, name='vueapp1'),
    path('api/test/user', joboard, name='vueapp2'),
    path('api/test/mod', joboard, name='vueapp3'),
    path('api/test/admin', joboard, name='vueapp4'),
    # Return 'Mods' model objects
    # path('mods/', ModsView.as_view(), name='mods_view'),
    # # Register a new user
    # path('register/', register, name='register_view'),
]
