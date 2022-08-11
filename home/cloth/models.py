from operator import length_hint
from django.db import models
from django.conf import settings

# Create your models here.
class Brand(models.Model):
    brand_name = models.CharField(max_length = 20, primary_key = True)
    contact = models.CharField(max_length = 11)
    address = models.CharField(max_length = 50)
    manager = models.CharField(max_length = 10)

class Product(models.Model):
    product_num = models.IntegerField(primary_key = True)
    product_name = models.CharField(max_length = 20, notnull=True)
    stock = models.IntegerField(null=True)
    price = models.SmallIntegerField(null=True)
    brand_name = models.ForeignKey(Brand, on_delete=models.CASCADE)
    supply_date = models.DateTimeField()
    supply_amount = models.IntegerField(null=True)


class Customer(models.Model):
    rank_select = (
        ('S', 'Silver'),
        ('G', 'Gold'),
        ('V', 'Vip'),
    )
    id = models.CharField(max_length = 10, primary_key = True)
    password = models.CharField(max_length = 15)
    name = models.CharField(max_length = 10)
    age = models.IntegerField(null=False)
    job = models.CharField(max_length = 15)
    rank = models.CharField(default= 'silver', max_length = 10, null=False, choices=rank_select)
    point = models.IntegerField(null=False, default=0)

class Post(models.Model):
    post_num = models.IntegerField(null=False, primary_key=True)
    title = models.CharField(max_length=30)
    body = models.TextField()
    user_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_date = models.DateTimeField()

class Order(models.Model):
    order_num = models.IntegerField(null=False, primary_key=True)
    product_num = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_amount = models.IntegerField(null=False)
    address = models.TextField(null=False, blank=False, max_length= 50)
    order_date = models.DateField(null=False, blank=False)