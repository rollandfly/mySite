from django.urls import path
from . import views

urlpatterns = [
    path('calculate/', views.calculatePage, name='calculatePage'),
]
