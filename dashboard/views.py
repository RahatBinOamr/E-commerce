from django.shortcuts import render,redirect
from product.models import Brand,Status,Category,CartItem
from dashboard.forms import ProductForm
# Create your views here.
def dashboard(request):
  return render(request, 'dashboard.html')

def add_product(request):
  categories= Category.objects.all()
  statuses= Status.objects.all()
  brands= Brand.objects.all()
  count = CartItem.objects.all().count()
  
  if request.method == "POST":
      forms = ProductForm(request.POST, request.FILES)
      if forms.is_valid():
        forms.save()
        return redirect('home')
  else:
      forms=ProductForm()
  context={
    'categories': categories,
    'statuses': statuses,
    'brands': brands,
    'forms': forms,
    'count': count,
  }
  return render(request, 'add_product.html',context)