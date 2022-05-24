from django.urls import path

from api.user import views

urlpatterns = [
    path('generations/', views.GenerationsList.as_view()),
    path('generations/<int:pk>/', views.GenerationsDetail.as_view()),
]