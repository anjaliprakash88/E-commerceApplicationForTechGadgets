from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .models import Product, CartItem


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "successfully registered")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "welcome")
                return redirect('product')
            else:
                messages.error(request, 'invaild')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('view_cart')

def view_cart(request):
    cart_items = CartItem.objects.all()
    return render(request, 'cart.html', {'cart_items': cart_items})


def removecart(request, product_id):
    product = get_object_or_404(Product, id = product_id)
    cart_item = get_object_or_404(CartItem, product=product)
    cart_item.delete()
    return redirect('view_cart')
