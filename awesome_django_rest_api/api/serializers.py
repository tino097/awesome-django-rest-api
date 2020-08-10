from rest_framework import serializers
from api.models import Company, Employee


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('name', 'address', 'city', 'country', 'email', 'phone')


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    company = CompanySerializer(many=False, read_only=True)

    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'company')