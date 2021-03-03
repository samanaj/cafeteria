from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
 
router = DefaultRouter()
router.register('categoria/add', CategoriaViewSet)

urlpatterns = [
    path('hello/', HelloView.as_view(), name='hello'),
    #path('categoria/add/', CategoriaViewSet.as_view(),name='add-categoria'),
]
urlpatterns += router.urls