from django.urls import path
from .views import UserRegistrationView, UserLoginView, ProductList, ProductDetail, InventoryItemList, InventoryItemDetail


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('items/', InventoryItemList.as_view(), name='inventoryitem-list'),
    path('items/<int:pk>/', InventoryItemDetail.as_view(), name='inventoryitem-detail'),
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
]
