from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import render, get_list_or_404

from .models import Product, Product_comment, Tag
from .serializers import ProductSerializer, ProductCommentSerializer, TagSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCommentViewSet(viewsets.ModelViewSet):
    queryset = Product_comment.objects.all()
    serializer_class = ProductCommentSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
