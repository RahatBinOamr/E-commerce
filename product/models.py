
from django.db import models
import uuid
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

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
    product_description =RichTextField(null=True, blank=True)
    product_image = models.ImageField(upload_to='productImages/')
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_status = models.ForeignKey(Status, on_delete=models.CASCADE)
    product_brand = models.ForeignKey(Brand, on_delete=models.CASCADE)


    def __str__(self) :
        return self.product_title
    





class CartItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.product.product_title}'






