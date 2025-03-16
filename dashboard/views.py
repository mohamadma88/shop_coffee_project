from django.shortcuts import render, get_object_or_404, redirect
from account.models import Address, User
from cart.models import Order
from cart.models import OrderItem
from product.models import Product, Like
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

def dashboard(request):
    if request.user.is_authenticated:
        # orders
        delivered = Order.objects.filter(user=request.user, status='Delivered')
        other_order = Order.objects.filter(user=request.user).exclude(status='Delivered')
        # address
        address = Address.objects.all()
        # favorite product
        favorite = request.user.like.values_list('product', flat=True)
        product = Product.objects.filter(id__in=favorite)[:3]
    return render(request, 'dashboard/dashboard.html',
                  {'delivered': delivered, 'other_order': other_order, 'address': address , 'product':product})


def dashboard_orders(request):
    if request.user.is_authenticated:
        delivered = Order.objects.filter(user=request.user, status='Delivered').order_by('-created_at')
        other_order = Order.objects.filter(user=request.user).exclude(status='Delivered').order_by('created_at')
        order_item = OrderItem.objects.all()
    return render(request, 'dashboard/dashboard_orders.html',
                  {'delivered': delivered, 'other_order': other_order, 'order_item': order_item})


def dashboard_address(request):
    address = Address.objects.all()
    return render(request, 'dashboard/dashboard-address.html', {'address': address})


def dashboard_detail_order(request, pk):
    if request.user.is_authenticated:
        order = Order.objects.get(id=pk)
        item = OrderItem.objects.filter(order=pk)
        return render(request, 'dashboard/dashboard_detail_orders.html', {'order': order, 'item': item})


def dashboard_favorite(request):
    favorite = request.user.like.values_list('product', flat=True)
    product = Product.objects.filter(id__in=favorite)
    return render(request, 'dashboard/dashboard-favorite.html', {'product':product})

