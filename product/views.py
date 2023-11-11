from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Brand,Category,Status,Product,Cart,CartItem
# Create your views here.
def HomePage(request):
    brands = Brand.objects.all()
    categories = Category.objects.all()
    statuses = Status.objects.all()
    products = Product.objects.all()
    count = CartItem.objects.all().count()
    for p in products:
        print(p)
    context={
        'brands':brands,
        'categories':categories,
        'statuses':statuses,
        'products':products,
        'count':count
    
    }
    return render(request, 'index.html',context)


def Product_DetailsPage(request,pk=None):
    product = Product.objects.get(id=pk)
    related_product = Product.objects.filter(product_category=product.product_category).values()
    
    context={
        'product':product,
        'related_product':related_product
    }
    return render(request,'product_details.html',context)


def Add_To_Cart(request,pk):
    user= request.user
    product= Product.objects.get(pk=pk)
    cart , _ = Cart.objects.get_or_create(user=user,is_paid=False)
    cart_item, created = CartItem.objects.get_or_create(pk=pk, cart=cart,product=product)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    else:
        cart_item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER') )


def Product_Cart(request):
    cart_items= CartItem.objects.all()
    totalPrice =[]
    for cart_item in cart_items:
        if cart_item.product.product_current_price:
            totalPrice.append(cart_item.product.product_current_price * cart_item.quantity)    
    context={
        'cart_items': cart_items,
        'totalPrice': sum(totalPrice),
        
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

def DashboardPage(request):
    return render(request,'dashboard.html')






def Register(request):
    m = ""
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        print(name, email, pass1, pass2)
        if (pass1 != pass2):
            m = "wrong password!!!"
        else:
            signUp = User.objects.create_user(
                username=name,
                email=email,
                password=pass1
            )
            signUp.save()
            return redirect('login')

    return render(request, 'register.html', {m: m})


def Login(request):
    m = ""
    if request.method == "POST":
        name = request.POST['name']
        password = request.POST['password']
        loginUser = authenticate(
            request,
            username=name,
            password=password
        )
        if loginUser is not None:
            login(request, loginUser)
            return redirect('/')
        else:
            m = "something went wrong"
    return render(request, 'login.html', {'m': m})


def LogOut(request):
    logout(request)
    return redirect('login')