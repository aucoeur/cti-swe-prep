from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def profile_user_view(*args, **kwargs):
    return HttpResponse('<h1>User Profile</h1>')
