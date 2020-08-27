from django.contrib import admin
from .models import *
# Import the class Customer

# Register your models here.
# Registering the table from the class Customer
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
