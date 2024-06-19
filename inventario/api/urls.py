from django.urls import path

from inventario.api.views import ProductAPIView, ProductDetailAPIView

urlpatterns = [
    path('products/', ProductAPIView.as_view(), name='products'),
    path('products-detail/<int:pk>/', ProductDetailAPIView.as_view(), name='products-detail'),
]
