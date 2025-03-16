from django.contrib import admin
from .models import Product, Category, AmountCaffeine, ProductReview , Like


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "discount", "best_selling")
    list_filter = ['create', 'price', 'discount', 'best_selling', 'amazing']
    search_fields = ['title','price']


@admin.register(ProductReview)
class ProductReview(admin.ModelAdmin):
    list_display = ('title', 'create')
    list_filter = ('create',)
    search_fields = ['title']



admin.site.register(Category)
admin.site.register(AmountCaffeine)
admin.site.register(Like)
