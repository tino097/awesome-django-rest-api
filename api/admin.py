from django.contrib import admin

# Register your models here.
from api.models import Company, Employee

# class CompanyAdmin(admin.ModelAdmin):
#     pass

# class EmployeeAdmin(admin.ModelAdmin):
#     pass

admin.site.register(Company)
admin.site.register(Employee)
