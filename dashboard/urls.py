from django.urls import path
from dashboard.views import dashboard,add_product
urlpatterns = [
  path('dashboard/',dashboard,name="dashboard"),
  path('add_product/',add_product,name="add_product"),
]
