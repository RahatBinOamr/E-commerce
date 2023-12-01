from django.contrib import admin
from .models import Category,Brand,Product,Status,CartItem,Review


class CategoryAdmin(admin.ModelAdmin):
  list_display=('created_at','updated_at','category_name' )
admin.site.register(Category, CategoryAdmin)


class StatusAdmin(admin.ModelAdmin):
  list_display=('created_at','updated_at','status')
admin.site.register(Status,StatusAdmin)


class BrandAdmin(admin.ModelAdmin):
  list_display=('created_at','updated_at','brand')
admin.site.register(Brand, BrandAdmin)



class ProductAdmin(admin.ModelAdmin):
  list_display=('created_at','updated_at','product_title','product_image','product_current_price', 'product_previous_price', 'product_quantity', 'product_offer', 'product_rating','product_description','product_category','product_status','product_brand')
admin.site.register(Product, ProductAdmin)


class CartItemAdmin(admin.ModelAdmin):
  list_display = ('product','quantity')

admin.site.register(CartItem,CartItemAdmin)

class ReviewAdmin(admin.ModelAdmin):
  list_display=('comment',)
admin.site.register(Review,ReviewAdmin)