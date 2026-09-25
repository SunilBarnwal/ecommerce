
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from .models import *
from django.http import JsonResponse
from django.db.models import Sum

# Create your views here.

def index_view(request):
    if not request.user.is_authenticated:
        return redirect('login_page')

    product=Products.objects.all()

    context = {'productdata': product,}

    return render(request, 'pages/index.html',context)

def courses_view(request):
    return render(request, 'pages/courses.html')

def login_view(request):    
    if request.method=='POST':
        print("Working in this view")
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        if not username or not password:
            messages.error(request,'please fill in all fields.')
            return redirect('login_page')
            
        user=User.objects.filter(username=username).first()
        
        if user is not None and user.check_password(password):
            login(request,user)
            messages.success(request,'Login Successful')
            return redirect('index_page')
        else:
            messages.error(request,'invalid username or password')
            return redirect('login_page')
    
    return render(request, 'pages/loginpage.html')

def register_view(request):
    if request.method == 'POST' :
        # Process the form data 
        user_name =request.POST.get('username')
        email = request.POST.get('email')
        password =request.POST.get('password')
        # mobile =request.POST.get('mobile')

        if not user_name or not email or not password:
            messages.error(request,'Please fill in all fields.')
            return redirect('register_page')

        if User.objects.filter(username=email).exists():
            messages.error(request,'Email already exist.')
            return redirect('register_page')

        user_data = User.objects.create_user(username=email, email=email, password=password ,first_name=user_name)
        user_data.save()
        messages.success(request,'Registration Successful')
        return redirect('login_page')

    return render(request, 'pages/registration.html')

def Logout_view(request):
    logout(request)
    messages.success(request,'You have been Logged Out Successfully')
    return redirect('login_page')

def forget_pass_view(request):

    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')

        if not username or not password or not confirm_password:
            messages.error(request,'Please fill in all fields.')
            return redirect('forget_pass_page')
        
        if password != confirm_password:
            messages.error(request,'Password not matched')
            return redirect('forget_pass_page')

        user_is =User.objects.filter(username=username).first()

        if user_is is not None:
            user_is.set_password(password)
            user_is.save()
            messages.success(request,'Password reset successful. Please login with new password')
            return redirect('login_page')


    return render( request,'pages/forget_pass.html')

def add_to_cart_view(request,product_id):
    if not request.user.is_authenticated:
        messages.error(request,'You need to be logged in to add items to the cart.')
        return redirect('login_page')

    productis= Products.objects.filter(id=product_id).first()

    if productis is None:
        messages.error(request,'Product not found.')
        return redirect('index_page')
    
    user_cart, created = UserCart.objects.get_or_create(user=request.user)

    cart_item, created = CartItems.objects.get_or_create(cart=user_cart, product=productis)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request,f'Added {productis.name} to your cart.')
    return redirect('index_page')

def cart_count(request):
    if not request.user.is_authenticated:
        messages.error(request,'You need to be logged in to view your cart.')
        return JsonResponse({'status': False, 'cart_count': 0})

    user_cart, created = UserCart.objects.get_or_create(user=request.user)
    cart_count = user_cart.cart_items.aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0
    return JsonResponse({
        'status': True,
        'cart_count': cart_count,
    })

def cart_items(request):
    if not request.user.is_authenticated:
        messages.error(request,'You need to be logged in to view your cart.')
        return redirect('login_page')

    user_cart, created = UserCart.objects.get_or_create(user=request.user)
    cart_items = user_cart.cart_items.select_related('product').all()

    total_items = sum(item.quantity for item in cart_items)
    subtotal = sum(item.product.price * item.quantity for item in cart_items)

    context = {
        'cart_items': cart_items,
        'total_items': total_items,
        'subtotal': subtotal,
        'total_amount': subtotal,
    }
    return render(request, 'pages/cart_items.html', context)


# def update_cart_item(request, product_id, action):

#     if not request.user.is_authenticated:
#         return redirect('login_page')

#     user_cart = get_object_or_404(
#         UserCart,
#         user=request.user
#     )

#     cart_item = get_object_or_404(
#         CartItems,
#         product_id=product_id,
#         cart=user_cart
#     )

#     if action == 'increase':
#         cart_item.quantity += 1
#         cart_item.save()

#     elif action == 'decrease':
#         if cart_item.quantity > 1:
#             cart_item.quantity -= 1
#             cart_item.save()
#         else:
#             cart_item.delete()

#     return redirect('cartItems')

def update_cart_item(request, product_id, action):

    if not request.user.is_authenticated:
        messages.error(
            request,
            'You need to be logged in to update your cart.'
        )
        return redirect('login_page')

    cart_item = CartItems.objects.filter(
        product_id=product_id,
        cart__user=request.user
    ).first()

    if cart_item is None:
        messages.error(request, 'Cart item not found.')
        return redirect('cartItems')

    if action == 'increase':
        cart_item.quantity += 1
        cart_item.save()

    elif action == 'decrease':
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
            messages.success(request, 'Item removed from cart.')

    return redirect('cartItems')
    

    
def view_details(request, product_id):
    product = get_object_or_404(Products, id=product_id)

    context = {
        'product': product,
    }
    return render(request, 'pages/viewdetails.html', context)