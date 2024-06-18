from django.urls import path

from inventario.api.views import ProductAPIView

urlpatterns = [
    path('products/', ProductAPIView.as_view(), name='products'),
]
