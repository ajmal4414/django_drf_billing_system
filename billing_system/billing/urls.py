from django.urls import path
from .views import (EmployeeListCreateView, 
EmployeeRetrieveUpdateDestroyAPIView,
ProductListCreateView,
ProductRetrieveUpdateDestroyAPIView,
CustomerListCreateView,
CustomerRetrieveUpdateDestroyAPIView,
BillListCreateView,
BillRetrieveUpdateDestroyAPIView,
LoginView)
urlpatterns=[
    path('login/',LoginView.as_view(), name='login'),
    path('employee/',EmployeeListCreateView.as_view(),name='employee-list'),
    path('employee/<int:pk>/', EmployeeRetrieveUpdateDestroyAPIView.as_view(),name='employee-detail'),
    path('products/',ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/',ProductRetrieveUpdateDestroyAPIView.as_view(),name='product-detail'),
    path('customers/',CustomerListCreateView.as_view(), name='customer-list'),
    path('customer/<int:pk>/',CustomerRetrieveUpdateDestroyAPIView.as_view(), name='customer-detail'),
    path('bill/',BillListCreateView.as_view(),name='bill-list'),
    path('bill/<int:pk>/',BillRetrieveUpdateDestroyAPIView.as_view(),name='bill=detail'),
    
]