from django.urls import path
from inventario.apiusd.views import MindicadorAPIView

urlpatterns = [
    path('data/<str:indicador>/<int:year>/', MindicadorAPIView.as_view(), name='mindicador-data'),
]
