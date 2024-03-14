from django.urls import path

from core.views import HomeView



urlpatterns = [
    path('', HomeView, name='home'),
]