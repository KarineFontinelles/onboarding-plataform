from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import *



urlpatterns = [
    # Auth
    path('token', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

    # Users
    path('users/', list_users),
    path('user', get_user),
    path('create-user/', create_user),

]



# https://plzhg0q6-8000.brs.devtunnels.ms/