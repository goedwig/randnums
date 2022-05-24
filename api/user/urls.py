from django.urls import path

from api.user import views

urlpatterns = [
    path('generations/', views.GenerationsListCreateAPIVIew.as_view()),
    path('generations/<int:pk>/', views.GenerationsRetrieveUpdateAPIView.as_view()),
    path('stats/', views.StatsAPIView.as_view()),
]