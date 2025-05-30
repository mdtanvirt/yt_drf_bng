from django.shortcuts import get_object_or_404
from api.serializers import ProductSerilizer
from api.models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serilizer = ProductSerilizer(products, many=True)
    return Response(serilizer.data)

@api_view(['GET'])
def products_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serilizer = ProductSerilizer(product)
    return Response(serilizer.data)