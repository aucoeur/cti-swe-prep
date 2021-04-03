from django.urls import path

from .views import PageDetailView

urlpatterns = [
    path('<str:slug>/', PageDetailView.as_view(), name='page-detail')
]
