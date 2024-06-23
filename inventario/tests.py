# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase

# class ProductIntegrationTest(APITestCase):
#     @mock.patch('inventario.models.Product.save', autospec=True)
#     def test_create_product_with_mock_db(self, mock_save):
#         # Simular datos de entrada
#         data = {
#             'product_name': 'Martillo',
#             'description': 'Un martillo robusto y confiable',
#             'price': 100,
#             'images': 'photos/products/Martillo_goma.jpg',
#             'stock': 50,
#             'is_available': True,
#             'category': 'Herramientas'
#         }
#         url = reverse('products')
#         # Realizar la petición POST para crear el producto
#         response = self.client.post(url, data, format='json')
        
#         # Verificar que el método save fue llamado.
#         mock_save.assert_called_once()
        
#         # Verificar que la respuesta sea correcta
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(response.data['product_name'], data['product_name'])
#         # Añade más aserciones según sea necesario para verificar los datos de respuesta

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from inventario.models import Product

class ProductoDetalleTestCase(APITestCase):
    def setUp(self):
        # Crear un producto de prueba en la base de datos
        self.product = Product.objects.create(
            product_name='Martillo',
            description='Un martillo robusto y confiable',
            price=100,
            stock=50,
            is_available=True,
            category='Herramientas'
        )

    def test_obtener_detalle_producto(self):
        # Construir la URL para el endpoint de detalle de producto
        url = reverse('products-detail', kwargs={'pk': self.product.pk})
        response = self.client.get(url)

        # Verificar que la respuesta sea exitosa
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verificar que los datos del producto sean correctos
        self.assertEqual(response.data['product_name'], 'Martillo')
        self.assertEqual(response.data['description'], 'Un martillo robusto y confiable')
        self.assertEqual(response.data['price'], 100)
        self.assertEqual(response.data['stock'], 50)
        self.assertEqual(response.data['is_available'], True)
        self.assertEqual(response.data['category'], 'Herramientas')