from django.shortcuts import render
from rest_framework import viewsets
from.models import Customer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CustomerSerializer

class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
