# from django.shortcuts import render
# from rest_framework import generics
# from .models import Products
# from .serializers import ProductsSerializer


# class ProductListView(generics.ListCreateAPIView):
#     queryset = Products.objects.all()
#     serializer_class =ProductsSerializer

from django.shortcuts import render
from rest_framework import generics
from .models import Products, OrderDetails
from .serializers import ProductsSerializer, OrderDetailsSerializer

class ProductListView(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer  # Added a space for consistency

class OrderDetailsListView(generics.ListCreateAPIView):
    queryset = OrderDetails.objects.all()
    serializer_class = OrderDetailsSerializer  # Added a space for consistency
