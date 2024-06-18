from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from inventario.api.serializers import ProductSerializer
from inventario.models import Product

class ProductAPIView(APIView):
    def get(self, request):
         products = Product.objects.all()
         serializer = ProductSerializer(products, many=True)
         return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        try:

            serializer = ProductSerializer(data=request.data)

            if serializer.is_valid():

                serializer.save()

                return Response({"mensaje":"Datos creados"}, status=status.HTTP_201_CREATED)
            else:
                # Devuelve una respuesta con los errores de validación
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(str(e))
            return Response({"mensaje": str(e)}, status=status.HTTP_400_BAD_REQUEST)  
       