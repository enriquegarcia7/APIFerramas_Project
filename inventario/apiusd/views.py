from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
import requests

class Mindicador:
    def __init__(self, indicador, year):
        self.indicador = indicador
        self.year = year
    
    def InfoApi(self):
        url = f'https://mindicador.cl/api/{self.indicador}/{self.year}'
        response = requests.get(url)
        data = json.loads(response.text.encode("utf-8"))
        return data

class MindicadorAPIView(APIView):
    def get(self, request, indicador, year):
        mindicador = Mindicador(indicador, year)
        data = mindicador.InfoApi()
        return Response(data, status=status.HTTP_200_OK)