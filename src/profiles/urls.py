from django.urls import path

from .views import profile_main_view, profile_user_view

urlpatterns = [
    path('', profile_main_view, name='profile-list-view'),
    path('<int:id>', profile_user_view, name='user-view'),
]
