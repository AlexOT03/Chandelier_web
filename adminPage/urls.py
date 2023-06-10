from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', views.indexAdmin.as_view(), name='indexAdmin'),
    path('admin/', include('estados.urls')),
    path('admin/', include('tematicas.urls')),
    # path('admin/', include('ubicaciones.urls')),
    # path('admin/', include('cotizacion.urls')),
    # path('admin/', include('servicios.urls')),
]