from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from api.serializers import CompanySerializer, EmployeeSerializer
from api.models import Company, Employee

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all().order_by('name')
    serializer_class = CompanySerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('last_name')
    serializer_class = EmployeeSerializer