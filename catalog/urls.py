from django.urls import path, include
from rest_framework import routers
from . import views
from rest_framework.routers import DefaultRouter
from .views import CategoryModelViewSet, ProductViewSet
router = DefaultRouter()
router.register('catalog',CategoryModelViewSet)
router.register('products',ProductViewSet, basename="products")
urlpatterns = [    
    path('',include(router.urls))
]
