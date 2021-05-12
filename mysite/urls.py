from django.contrib import admin
from django.urls import path, include
from register import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('todo.urls')),
    path('', include("django.contrib.auth.urls")),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="register"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('weather.urls')),
    path('',include('calculate.urls')),
]
