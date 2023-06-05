from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexHome.as_view(), name='indexHome'),
    path('fast-quote/', views.fastQuoteHome.as_view(), name='fastQuoteHome'),
    path('location/<int:id>/<str:name>', views.locationHome.as_view(), name='locationHome'),
    path('location/info/<int:id>/', views.locationInfoHome.as_view(), name='locationInfoHome'),
    path('quote/<id>', views.quoteHome.as_view(), name='quoteHome'),
    path('about-us/', views.aboutUsHome.as_view(), name='aboutHome'),
    path('contact-us/', views.contactHome.as_view(), name='contactHome'),
]