from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Category
from .serializers import CategorySerializer


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
