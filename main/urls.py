from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.homePage , name='home'),
    path('home/', views.homePage , name='home'),
    path('contact/', views.contactPage, name='contact'),
]
