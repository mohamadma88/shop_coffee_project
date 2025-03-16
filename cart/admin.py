from django.contrib import admin
from .views import Order,OrderItem

admin.site.register(Order)
admin.site.register(OrderItem)