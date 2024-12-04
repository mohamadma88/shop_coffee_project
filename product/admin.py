from django.contrib import admin
from .models import Product, Category, AmountCaffeine, ProductReview


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "discount", "best_selling")
    list_filter = ['create', 'price', 'discount', 'best_selling', 'amazing']


@admin.register(ProductReview)
class ProductReview(admin.ModelAdmin):
    list_display = ('title', 'create')
    list_filter = ('create',)


admin.site.register(Category)
admin.site.register(AmountCaffeine)
