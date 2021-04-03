from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth.models import User
from .models import Profile

# Create your views here.
def profile_main_view(*args, **kwargs):
    users = Profile.objects.all()

    return HttpResponse(f'<h1>User Profile</h1><div>{users}</div>')

def profile_user_view(*args, **kwargs):
    return HttpResponse(Profile.objects.get(id=kwargs['id']))
