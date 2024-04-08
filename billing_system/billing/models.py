from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Employee(AbstractUser):
    designation=models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Product(models.Model):
    name= models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Bill(models.Model):
    customer = models.ForeignKey(Customer, on_delete= models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete= models.CASCADE)
    products = models.ManyToManyField(Product, through="BillItem")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Bill for {self.customer} by {self.employee}"

class BillItem(models.Model):
    bill = models.ForeignKey(Bill, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} * {self.product} in Bill {self.bill.id}"

