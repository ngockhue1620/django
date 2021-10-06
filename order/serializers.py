
from django.db.models import fields
from rest_framework import serializers
from .models import *
class OrderDetailSerializer(serializers.ModelSerializer):
  class Meta:
    model =OrderDetail
    fields = ['id', 'product', 'price', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
  class Meta: 
    model= Order
    fields = '__all__'