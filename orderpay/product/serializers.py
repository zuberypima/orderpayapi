from rest_framework import serializers
from .models import Products, OrderDetails

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['title', 'BuyingPrice', 'sellingprice', 'quantity', 'description'] 

class OrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = ['product','order_number', 'table_number', 'createdDate'] 

