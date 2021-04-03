from django.urls import path

from .views import profile_user_view

urlpatterns = [
    path('', profile_user_view, name='profile')
]
