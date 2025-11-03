from django.shortcuts import get_object_or_404
from api.serializers import ProductSerilizer, OrderSerilizer
from api.models import Product, Order, OrderItem
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics

from rest_framework import viewsets

class product_list(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerilizer

class orders_list(viewsets.ModelViewSet):
    queryset = Order.objects.all().prefetch_related('items__product')
    serializer_class = OrderSerilizer