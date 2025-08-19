from product.models import Product
from django.contrib import messages

CART_SESSION_ID = 'cart'


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        cart = self.cart.copy()

        for item in cart.values():
            product = Product.objects.get(id=int(item['id']))
            item['product'] = Product.objects.get(id=int(item['id']))
            item['total'] = int(item['quantity']) * int(item['price'])
            item['unique_id'] = self.unique_id_generator(product.id)
            yield item

    def unique_id_generator(self, id):
        result = f'{id}'
        return result

    def add(self, product, quantity, request=None):

        unique = self.unique_id_generator(product.id)
        try:
            quantity = int(quantity)
        except:
            quantity = 1

        max_allowed = 5
        if product.stock < 3:
            max_allowed = product.stock

        quantity = min(quantity, max_allowed)

        if unique not in self.cart:
            self.cart[unique] = {
                'quantity': 0,
                'price': str(product.price),
                'id': str(product.id)
            }

        new_quantity = self.cart[unique]['quantity'] + quantity

        if new_quantity > max_allowed:
            new_quantity = max_allowed
            if request:
                messages.warning(request, f"حداکثر تعداد قابل خرید برای این محصول {max_allowed} عدد است.")

        self.cart[unique]['quantity'] = new_quantity
        self.session.modified = True

        if request:
            messages.success(request,
                             f"{product.name} به سبد خرید اضافه شد (تعداد: {self.cart[unique]['quantity']})")

    def total(self):
        cart = self.cart.values()
        total = sum(int(item['price']) * int(item['quantity']) for item in cart)
        return total

    def remove_cart(self):
        del self.session[CART_SESSION_ID]

    def delete(self, id):
        if id in self.cart:
            del self.cart[id]
        self.save()

    def save(self):
        self.session.modified = True
