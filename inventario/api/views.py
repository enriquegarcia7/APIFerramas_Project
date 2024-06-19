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


class ProductDetailAPIView(APIView):

    def patch(self, request, pk):
        try:
            product = Product.objects.get(id=pk)
            # Utiliza partial=True para permitir la actualización parcial
            serializer = ProductSerializer(product, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response({"mensaje": "Datos actualizados"}, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Product.DoesNotExist:
            return Response({"mensaje": "Producto no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            product = Product.objects.get(id=pk)
            product.delete()
            return Response({"mensaje": "Producto eliminado"}, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"mensaje": "Producto no encontrado"}, status=status.HTTP_404_NOT_FOUND)