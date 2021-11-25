from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from joboard.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # Path to obtain a new access and refresh token
    path('api/auth/signin', MyTokenObtainPairView.as_view(), name='login'),
    path('api/auth/signup', register, name='signup'),
    path('api/auth/signout', LogoutView.as_view(), name="signout"),
    # Submit your refresh token to this path to obtain a new access token
    path('api/auth/refreshtoken', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/candidates', CandidatesView.as_view(), name='vueapp'),
    path('api/candidates/<int:id>', CandidateDetailView.as_view(), name='vueapp'),
]
