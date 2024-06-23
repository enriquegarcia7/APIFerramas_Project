import json
from unittest import TestCase
from unittest.mock import patch
from inventario.apiusd.views import Mindicador

class TestMindicador(TestCase):
    @patch('inventario.apiusd.views.requests.get')
    def test_InfoApi_success(self, mock_get):
        # Simula una respuesta exitosa de la API
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.text = json.dumps({
            'version': '1.6.0',
            'autor': 'mindicador.cl',
            'codigo': 'dolar',
            'nombre': 'Dólar observado',
            'unidad_medida': 'Pesos',
            'serie': [{'fecha': '2023-04-10T00:00:00.000Z', 'valor': 750.2}]
        })
        
        mindicador = Mindicador('dolar', '2023')
        data = mindicador.InfoApi()
        
        # Verifica que la respuesta contiene la información esperada
        self.assertEqual(data['codigo'], 'dolar')
        self.assertEqual(data['serie'][0]['valor'], 750.2)

    @patch('inventario.apiusd.views.requests.get')
    def test_InfoApi_failure(self, mock_get):
        # Simula una respuesta fallida de la API
        mock_response = mock_get.return_value
        mock_response.status_code = 404
        mock_response.text = json.dumps({'error': 'Indicador no encontrado'})
        
        mindicador = Mindicador('inexistente', '2023')
        data = mindicador.InfoApi()
        
        # Verifica que la respuesta contiene el mensaje de error esperado
        self.assertEqual(data['error'], 'Indicador no encontrado')