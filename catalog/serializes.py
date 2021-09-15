from .models import Category, Product
from django.db import models
from django.db.models import fields
from rest_framework import serializers

class CategorySerialize(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Category

class ProductSerialize(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Product
