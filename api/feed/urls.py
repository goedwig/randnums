from django.urls import path

from api.feed import views

urlpatterns = [
    path('', views.FeedList.as_view()),
]
