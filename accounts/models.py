from django.db import models
# Allow to create classes that create database tables.
#
# Create your models here.

# String values are specified as --> Charfield .
# DateTimeField -->Lets THe user know when a specific Item was loaded.
# Null = True -->Allows us to make changes into our database, 
# Allows to import customer with maybe just a name and no phone or email or date created. 
# If null is not set to true There will be an error and we will be forced to add a defult value.
class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    # Return name for it to display it in the admin panel
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    # Return name for it to display it in the admin panel
    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('Indooor', 'Indooor'),
        ('Out door', 'Out door'),
        )

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out of delivery', 'Out of delivery'),
        ('Delivered', 'Delivered'),
        )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)# on_delete=models.SET_NULL --> When an order is removed the order will remain in the database
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)# on_delete=models.SET_NULL --> When an order is removed the order will remain in the database
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.product.name
