from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexHome.as_view(), name='indexHome'),
    path('fast-quote/', views.quoteHome.as_view(), name='fastQuoteHome'),
    path('location/<id>/', views.locationHome.as_view(), name='locationHome'),
    path('location/info/<id>/', views.locationInfoHome.as_view(), name='locationInfoHome'),
    path('about-us/', views.aboutUsHome.as_view(), name='aboutHome'),
    path('contact-us/', views.contactHome.as_view(), name='contactHome'),
]