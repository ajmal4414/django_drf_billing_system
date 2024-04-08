from rest_framework import serializers
from .models import Employee, Product, Customer, BillItem, Bill


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields= ('id', 'username', 'designation')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields =('id', 'name', 'price', 'description')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'email', 'phone' , 'address')

class BillItemSerializer(serializers.ModelSerializer):
    Product = ProductSerializer
    class Meta:
        model = BillItem
        fields = ('id', 'bill', 'product', 'quantity', 'amount')

class BillSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()
    # product = ProductSerializer()
    items = BillItemSerializer(source="billitem_set" ,many=True, read_only= True)
    class Meta:
        model = Bill
        fields = ('id', 'employee', 'customer',  'total_amount', 'created_at','items')