from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from unittest import mock
from django.core.files.uploadedfile import SimpleUploadedFile

class ProductTestCase(APITestCase):
    @mock.patch('inventario.models.Product.save', autospec=True)
    def test_create_product(self, mock_save):
        # Crear una imagen en memoria para simular la carga de archivos
        image = SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg')
        
        data = {
            'product_name': 'Martillo',
            'description': 'Un martillo robusto y confiable',
            'price': 100,
            'images': image,
            'stock': 50,
            'is_available': True,
            'category': 'Herramientas'
        }
        url = reverse('products')
        # Realizar la petición POST para crear el producto, usando multipart para soportar archivos
        response = self.client.post(url, data, format='multipart')
        
        # Verificar que el método save fue llamado.
        mock_save.assert_called_once()
        
        # Verificar que la respuesta sea correcta
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['product_name'], data['product_name'])
        # Añade más aserciones según sea necesario para verificar los datos de respuesta