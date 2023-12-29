""" from product.models import CartItem
def count(request):
  count = count = CartItem.objects.filter(user=request.user,is_paid=False).count()
  context={'count': count}
  if request.user.is_authenticated:
      return context """