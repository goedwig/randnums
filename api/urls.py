from django.urls import path, include

urlpatterns = [
    path('auth/', include('api.auth.urls')),
    path('feed/', include('api.feed.urls')),
    path('user/', include('api.user.urls')),
]
