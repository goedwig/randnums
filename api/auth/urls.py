from django.urls import path
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh

from api.auth.views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('token/', token_obtain_pair),
    path('token/refresh/', token_refresh),
]
