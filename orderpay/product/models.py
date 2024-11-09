from django.db import models
from django.utils import timezone

# Create your models here.

class Products(models.Model):
    title =models.CharField(max_length=200)
    BuyingPrice=models.CharField(max_length=200)
    sellingprice =models.CharField(max_length=200)
    quantity =models.IntegerField()
    description=models.TextField()
    def __str__(self):
        return self.title


class OrderDetails(models.Model):
    product =models.ForeignKey(Products, on_delete=models.CASCADE ,related_name='product_name')
    order_number=models.CharField(max_length=200)
    table_number =models.CharField(max_length=200)
    createdDate =models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.order_number