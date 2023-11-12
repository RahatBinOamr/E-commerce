from django.db import models
import uuid
from django.contrib.auth.models import User

# category models
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

# Status Models
class Status(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=200)

    def __str__(self):
        return self.status

# Brand Models
class Brand(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    brand = models.CharField(max_length=200)

    def __str__(self):
        return self.brand


# Product models
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product_title= models.CharField(max_length=250)
    product_current_price=models.IntegerField(default=0)
    product_previous_price=models.IntegerField(default=0)
    product_quantity=models.IntegerField(default=0)
    product_rating = models.IntegerField(default=0)
    product_offer=models.IntegerField(default=0)
    product_description = models.TextField()
    product_image = models.ImageField(upload_to='productImages/')
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_status = models.ForeignKey(Status, on_delete=models.CASCADE)
    product_brand = models.ForeignKey(Brand, on_delete=models.CASCADE)


    def __str__(self) :
        return self.product_title
    


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    

    



class CartItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cart= models.ForeignKey(Cart, null=True, blank=True,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    







