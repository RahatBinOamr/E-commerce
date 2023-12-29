from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from UserProfile.models import Profile
from .models import Brand,Category,Status,Product,CartItem,Review
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from product.forms import ReviewForm
from django.contrib.auth.decorators import login_required



# Create your views here.

def HomePage(request):
    
    brands = Brand.objects.all()
    categories = Category.objects.all()
    statuses = Status.objects.all()



    # searching the  products 
    if request.method == 'GET':
            query_s = request.GET.get('search')
            query_c = request.GET.get('search')
            query_b = request.GET.get('search')
            if query_s or query_c or query_b:
                querySet= (Q(product_title__contains =query_s)) | (Q(product_brand__brand=query_b)) | (Q(product_category__category_name=query_c))
                products = Product.objects.filter(querySet).distinct()
            else:
                products = Product.objects.all().order_by('?')


    # filtering by category,brand,status
    if request.method == 'GET':
            selected_category = request.GET.get('category')
            selected_brand = request.GET.get('brand')
            selected_status = request.GET.get('status')
            if selected_category or selected_brand or selected_status:
                querySet= (Q(product_category__category_name =selected_category)) | (Q(product_brand__brand=selected_brand)) | (Q(product_status__status=selected_status))
                products = Product.objects.filter(querySet).distinct()
            else:
                products = Product.objects.all().order_by('?')

    # pagination
    items_per_page = 6
    paginator = Paginator(products, items_per_page)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    # Upcoming Product
    upcoming = Product.objects.filter(product_status__status="Up-Comming")
    mobile = Product.objects.filter(product_category__category_name="Mobile")
    laptop = Product.objects.filter(product_category__category_name="Laptop")

    context={
        'brands':brands,
        'categories':categories,
        'statuses':statuses,
        'products':products,
        'upcoming':upcoming,
        'mobile':mobile,
        'laptop':laptop,
    
    }
    return render(request, 'index.html',context)


def Product_DetailsPage(request,pk=None):
    product = get_object_or_404(Product, id=pk)
    related_product = Product.objects.filter(Q(product_category=product.product_category)| Q(product_brand=product.product_brand)).exclude(id=product.id)


    reviews = Review.objects.filter(product=product)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user  
            review.product = product

            review.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER') )

    else:
        form = ReviewForm()
    context={
        'product':product,
        'related_product':related_product,
        'form':form,
        'reviews':reviews,
        
    }
    return render(request,'product_details.html',context)

@login_required
def Add_To_Cart(request,pk=None):
    product= Product.objects.get(pk=pk)
    cart_item, created = CartItem.objects.get_or_create( user=request.user,product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    else:
        cart_item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER') )


def Product_Cart(request):
    cart_items= CartItem.objects.filter(user=request.user)
    count = CartItem.objects.filter(user=request.user).count()
    
    totalPrice =[]
    for cart_item in cart_items:
        if cart_item.product.product_current_price:
            totalPrice.append(cart_item.product.product_current_price * cart_item.quantity)    
    context={
        'cart_items': cart_items,
        'totalPrice': sum(totalPrice),
        'count':count,
        
    }
    return render(request,'cart.html', context)

def increment_quantity(request, pk):
    item = get_object_or_404(CartItem, id=pk)
    item.quantity += 1
    item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER') )

def decrement_quantity(request, pk):
    item = get_object_or_404(CartItem, id=pk)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER') )



def remove_cart_item(request,pk):
    item = get_object_or_404(CartItem, id=pk)
    item.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER') )

def reset_cart(request):
    CartItem.objects.all().delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER') )



def check_out_cart(request):
    cart_items=cart_items= CartItem.objects.filter(user=request.user)

    totalPrice=0;
    for item in cart_items:
        totalPrice=totalPrice+item.product.product_current_price*item.quantity
    context={
        'cart_items': cart_items,
        'totalPrice': totalPrice,
    }
    return render(request,'checkout.html',context)



def not_found(request,exception):
    return render(request,'notfound.html')





