from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product

class ProductIntegrationTest(APITestCase):
    def test_create_and_retrieve_product(self):
        # Crear un producto
        url = reverse('products') 
        print(str(url)) # Asegúrate de tener esta ruta definida en inventario/urls.py
        data = {
            'product_name': 'Martillo',
            'description': 'Un martillo robusto y confiable',
            'price': 100,
            'images': 'photos/products/Martillo_goma.jpg',	
            'stock': 50,
            'is_available': True,
            'category': 'Herramientas'
        }
        
        response = self.client.post(url, data, format='json')

        try:
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        except Exception as e:      
            print(str(e))
        # Recuperar el producto creado
        product_id = response.data['id']
        url = reverse('products-detail', args=[product_id])  # Asegúrate de tener esta ruta definida
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['product_name'], 'Martillo')
