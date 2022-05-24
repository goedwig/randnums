from django.urls import path, include

urlpatterns = [
    path('feed/', include('api.feed.urls')),
    path('user/', include('api.user.urls')),
]
