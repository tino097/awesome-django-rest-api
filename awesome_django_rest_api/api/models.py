from django.db import models

# Create your models here.
class Company(models.Model):
    '''
    Company entity
    '''
    name = models.CharField(max_length=20, unique=True)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, null=True)
    phone = models.CharField(max_length=15, null=True)

    def __str__(self):
        return '%s' % self.name


class Employee(models.Model):
    '''
    Employee entity
    '''

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    company = models.OneToOneField(Company, on_delete=models.CASCADE)

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)