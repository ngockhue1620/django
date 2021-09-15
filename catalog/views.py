from django.shortcuts import render

from django.http import HttpResponse
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from .models import Category, Product
from .serializes import CategorySerialize, ProductSerialize
from rest_framework import status

class CategoryModelViewSet(viewsets.ModelViewSet):
    # tự động hổ trợ mình viết những api cở bản 
    # list (lấy tất cả category)
    # post (thêm 1 category)
    # put (cập nhập 1 category)
    # delete (xóa 1 category)
    # retrive (tìm 1 category)
    queryset = Category.objects.all()
    serializer_class = CategorySerialize
    
    # databse 
class ProductViewSet(viewsets.ViewSet):

    def list(self, request):
        products = Product.objects.all()
        serialize = ProductSerialize(products, many =True)
        return Response(serialize.data,status=status.HTTP_200_OK)

    def create(self, request):        
        serialize = ProductSerialize(data=request.data)
        if serialize.is_valid():
            serialize.save
            return Response(serialize.data, status =status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass    

    def destroy(self, request, pk=None):
        pass


