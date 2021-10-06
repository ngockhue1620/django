from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet
router = DefaultRouter()
router.register('',OrderViewSet, 'order')
urlpatterns = [    
    path('',include(router.urls))
]
