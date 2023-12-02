from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from UserProfile.models import UserProfile
from .models import Brand,Category,Status,Product,CartItem,Review
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from product.forms import ReviewForm, UserProfileForm,UserRegistrationForm,LoginForm
# Create your views here.
def HomePage(request):
    brands = Brand.objects.all()
    categories = Category.objects.all()
    statuses = Status.objects.all()
    count = CartItem.objects.filter(user=request.user).count()
    user_profile = UserProfile.objects.get(user=request.user)
    user_authenticated = User.is_authenticated
    user_active = User.is_active

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


    context={
        'brands':brands,
        'categories':categories,
        'statuses':statuses,
        'products':products,
        'count':count,
        'user_authenticated':user_authenticated,
        'user_active':user_active,
        'user_profile':user_profile,
    
    }
    return render(request, 'index.html',context)


def Product_DetailsPage(request,pk=None):
    product = get_object_or_404(Product, id=pk)
    related_product = Product.objects.filter(product_category=product.product_category).values()
    count = CartItem.objects.filter(user=request.user).count()
    user_profile = UserProfile.objects.get(user=request.user)
    reviews = Review.objects.filter(product=product)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user  
            review.product = product
            review.profile = user_profile
            review.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER') )

    else:
        form = ReviewForm()
    context={
        'product':product,
        'related_product':related_product,
        'count':count,
        'form':form,
        'reviews':reviews,
        'user_profile':user_profile
    }
    return render(request,'product_details.html',context)


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
    user_profile = UserProfile.objects.get(user=request.user)
    totalPrice =[]
    for cart_item in cart_items:
        if cart_item.product.product_current_price:
            totalPrice.append(cart_item.product.product_current_price * cart_item.quantity)    
    context={
        'cart_items': cart_items,
        'totalPrice': sum(totalPrice),
        'count':count,
        'user_profile': user_profile
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
    count = CartItem.objects.filter(user=request.user).count()
    user_profile = UserProfile.objects.get(user=request.user)
    totalPrice=0;
    for item in cart_items:
        totalPrice=totalPrice+item.product.product_current_price*item.quantity
    context={
        'cart_items': cart_items,
        'totalPrice': totalPrice,
        'count': count,
        'user_profile': user_profile
    }
    return render(request,'checkout.html',context)



def Register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('home') 
    else:
        user_form = UserRegistrationForm()
        profile_form = UserProfileForm()
    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form})


def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the home page or any other desired page after login
            else:
                form.add_error(None, 'Invalid login credentials')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def LogOut(request):
    logout(request)
    return redirect('login') 