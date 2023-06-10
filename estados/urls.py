from django.urls import path, include
from . import views

urlpatterns = [
    path('states/', views.StatesAdminView.as_view(), name='statesAdmin')
]