from django.urls import path
from . import views

urlpatterns = [
    path('weather/', views.weatherPage, name='weatherPage'),
]
