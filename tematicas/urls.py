from django.urls import path, include
from . import views

urlpatterns = [
    path('thems/', views.ThemAdminView.as_view(), name='themsAdmin')
]