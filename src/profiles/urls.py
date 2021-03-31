from django.urls import path

from .views import profile_user

urlpatterns = [
    path('', profile_user, name='profile')
]
