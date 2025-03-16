from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .cart_module import Cart
from product.models import Product
from .models import Order, OrderItem


class CartView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'cart/shopping-cart.html', {'cart': cart})


class AddCart(View):
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        quantity = request.POST.get('quantity')
        cart = Cart(request)
        cart.add(product, quantity)

        return redirect('cart:cart')


class CartDelete(View):
    def get(self, request, id):
        cart = Cart(request)
        cart.delete(id)
        return redirect('cart:cart')


class OrderDetail(View):
    def get(self, request, pk):
        order = get_object_or_404(Order, id=pk)
        return render(request, 'cart/payment.html', {'order': order})


class OrderCreation(View):
    def get(self, request):
        cart = Cart(request)
        order = Order.objects.create(user=request.user, total_price=cart.total())
        for item in cart:
            OrderItem.objects.create(order=order, product=item['product'], quantity=item['quantity'],
                                     price=item['price'])

            cart.remove_cart()
            return redirect('cart:order', order.id)



