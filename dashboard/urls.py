from django.urls import path
from dashboard.views import dashboard,add_product,product_collections,remove_product,update_product
urlpatterns = [
  path('dashboard/',dashboard,name="dashboard"),
  path('add_product/',add_product,name="add_product"),
  path('product_collection/',product_collections,name="product_collection"),
  path('remove_product/<pk>',remove_product,name="remove_product"),
  path('update_product/<pk>',update_product,name="update_product"),
]
