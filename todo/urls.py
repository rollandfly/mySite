from django.urls import path
from . import views

urlpatterns = [
    path('viewList/', views.viewListPage, name='viewList'),
    path('viewList/<str:id>', views.viewDetailPage, name='viewDetail'),
]
