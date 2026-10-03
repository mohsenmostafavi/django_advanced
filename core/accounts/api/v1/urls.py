from django.urls import path, include

# from rest_framework.authtoken.views import ObtainAuthToken
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

app_name = "api_v1"

urlpatterns = [
    # registeration
    path("register/", views.RegisterationApiView.as_view(), name="register"),
    # Using token
    path("token/login/", views.CustomObtainAuthToken.as_view(), name="token_login"),
    path("token/logout/", views.CustomDiscardAuthToken.as_view(), name="token_logout"),
    # change password
    path("change-password", views.ChangePasswordApiView.as_view(), name="change_pass"),
    # reset password
    # login session
    path("jwt/create/", views.CustomTokenObtainPairView.as_view(), name="jwt_create"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt_refresh"),
    path("jwt/verfiy/", TokenVerifyView.as_view(), name="jwt_verify"),
]
