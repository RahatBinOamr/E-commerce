from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from product.models import Brand,Status,Category,CartItem,Product
from dashboard.forms import ProductForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# Create your views here.
def dashboard(request):
  return render(request, 'dashboard.html')

def add_product(request):
  categories= Category.objects.all()
  statuses= Status.objects.all()
  brands= Brand.objects.all()
  count = CartItem.objects.filter(user=request.user).count()
  if request.method == "POST":
      forms = ProductForm(request.POST, request.FILES)
      if forms.is_valid():
        forms.save()
        return redirect('product_collection')
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

def product_collections(request):
    products=Product.objects.all()
    count = CartItem.objects.filter(user=request.user).count()



  # searching the  products 
    query = request.GET.get('search')
    if query:
        products = Product.objects.filter(Q(product_title__contains=query) )
    else:
        products = Product.objects.all().order_by('-id')



    # pagination
    items_per_page = 5
    paginator = Paginator(products, items_per_page)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context={
        'products': products,
        'count': count,
    }
    return render(request, 'product_collection.html',context)

def remove_product(request,pk=None):
    item = get_object_or_404(Product, id=pk)
    item.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER') )

def update_product(request,pk=None):
    product = get_object_or_404(Product, id=pk)
    if request.method == "POST":
        forms = ProductForm(request.POST, request.FILES, instance=product)
        if forms.is_valid():
            forms.save()
            return redirect('product_collection')
    else:
        forms = ProductForm(instance=product)

    context={
        'forms':forms
    }
    return render(request, 'update_product.html',context)