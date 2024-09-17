from django.shortcuts import render
from rest_framework import viewsets

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ('get', 'post',)


def index(request):
    return render(request, '../templates/index.html')
