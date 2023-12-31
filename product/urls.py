from django.urls import path 
from .views import HomePage,Product_DetailsPage,Add_To_Cart,Product_Cart,increment_quantity, decrement_quantity,remove_cart_item,reset_cart,check_out_cart

urlpatterns = [
    path('',HomePage,name='home'),
    path('details/<pk>',Product_DetailsPage,name='Product_Details'),
    path('add-to-cart/<pk>',Add_To_Cart,name='add_to_cart'),
    path('cart/',Product_Cart,name='cart'),

    path('increment_quantity/<pk>/', increment_quantity, name='increment_quantity'),
    path('decrement_quantity/<pk>/', decrement_quantity, name='decrement_quantity'),
    path('remove_cart_item/<pk>', remove_cart_item, name='remove_cart_item'),

    path('reset_cart/',reset_cart, name='reset_cart'),

    path('check-out',check_out_cart, name='check_out_cart'),


    
]
