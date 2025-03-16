import datetime

from django.db import models
from account.models import User
from product.models import Product


class Order(models.Model):
    ORDER_STATUS = [
        ('Pending', 'در حال پرداخت'),
        ('Processing', 'در حال پردازش'),
        ('Shipped', 'در حال ارسال'),
        ('Delivered', 'تحویل داده شده'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    total_price = models.IntegerField(default=0)
    is_paid = models.BooleanField(default=False)
    status = models.CharField(max_length=100, choices=ORDER_STATUS, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True)

    def save(self, *args,**kwargs):
        if self.pk:
            old_status = Order.objects.get(id=self.pk,).status
            if old_status != self.status:
                self.updated = datetime.datetime.now()
        super().save(*args,**kwargs)

    def __str__(self):
        return self.user.phone


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
    quantity = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
