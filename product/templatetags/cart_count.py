from django  import template
from product.models import CartItem
register = template.Library()
@register.filter()
def cart_count(user):
  if user.is_authenticated:
    cart_count = CartItem.objects.filter(user=user,is_paid=False).count()
    return cart_count
  
  else:
    return 0
