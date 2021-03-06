# api/urls.py
from django.urls import include, path

urlpatterns = [
    path('chat/', include('chat.urls')),
    path('users/', include('users.urls')),
    path('friends/', include('friends.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]