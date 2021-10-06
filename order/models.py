from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField
from catalog.models import Product
from user.models import User
# Create your models here.
class Order(models.Model):
  address = CharField(max_length=255)
  note = CharField(max_length=255)
  user = models.ForeignKey(User, related_name='orders', on_delete=models.SET_NULL, null=True)

class OrderDetail(models.Model):
  order = models.ForeignKey(Order, related_name='order_details', on_delete=models.CASCADE)
  product = models.ForeignKey(Product, related_name='order_detail', on_delete=models.SET_NULL, null=True)
  price = models.BigIntegerField()
  quantity = models.IntegerField()