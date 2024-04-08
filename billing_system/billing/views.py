from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView
from drf_spectacular.utils import extend_schema
from .models import Employee, Product, Customer, Bill, BillItem 
from .serializers import EmployeeSerializer, ProductSerializer, CustomerSerializer, BillItemSerializer, BillSerializer
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework .response import Response
# Create your views here.

class EmployeeListCreateView(generics.ListCreateAPIView):
    permission_classes =()
    authentication_classes= ()
    queryset= Employee.objects.all
    serializer_class= EmployeeSerializer
    @extend_schema(responses=EmployeeSerializer)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    @extend_schema(request= EmployeeSerializer, responses=EmployeeSerializer)
    def post(self, request,  **kwargs):
        return self.create(request, **kwargs)

class EmployeeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = ()
    authentication_classes=()
    queryset = Employee.objects.all()
    serializer_class= EmployeeSerializer

    @extend_schema(responses=EmployeeSerializer)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    @extend_schema(request=EmployeeSerializer, responses=EmployeeSerializer)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class ProductListCreateView(generics.ListCreateAPIView):
    permission_classes=()
    authentication_classes=()
    queryset=Product.objects.all()
    serializer_class =ProductSerializer
    @extend_schema(responses=ProductSerializer)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    @extend_schema(request=ProductSerializer, responses=ProductSerializer)
    def post(self, request, **kwargs):
        return self.create(request, **kwargs)

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=()
    authentication_classes=()
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @extend_schema(responses=ProductSerializer)
    def get(self,request, *args, **kwargs):
        return self.retrieve(request, *args, *kwargs)

    @extend_schema(request=ProductSerializer, responses=ProductSerializer)
    def put(self, request, *args ,**kwargs):
        return self.update(request, *args, **kwargs)
    
class CustomerListCreateView(generics.ListCreateAPIView):
    permission_classes=()
    authentication_classes=()
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    @extend_schema(responses=CustomerSerializer)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    @extend_schema(request=CustomerSerializer, responses=CustomerSerializer)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CustomerRetrieveUpdateDestroyAPIView(generics.RetrieveDestroyAPIView):
    permission_classes=()
    authentication_classes=()
    queryset = Customer.objects.all()
    serializer_class=CustomerSerializer
    
    @extend_schema(responses=CustomerSerializer)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    @extend_schema(request=CustomerSerializer, responses=CustomerSerializer)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class BillListCreateView(generics.ListCreateAPIView):
    permission_classes=()
    authentication_classes=()
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

    @extend_schema(responses=BillSerializer)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @extend_schema(request=BillSerializer, responses=BillSerializer)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class BillRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=()
    authentication_classes=()
    queryset =Bill.objects.all()
    serializer_class =BillSerializer

    @extend_schema(responses=BillSerializer)
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    @extend_schema(request=BillSerializer, responses=BillSerializer)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)



class LoginView(TokenObtainPairView):
    def post(self,request, *args, **kwargs):
        response = super().post (request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            token = response.data['access']
            return Response ({token:token},status=status.HTTP_200_OK)
        else:
            return Response({'error':'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


