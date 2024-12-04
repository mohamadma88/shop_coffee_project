from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, TemplateView, ListView
from product.models import Product, Category, ProductReview


def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        ProductReview.objects.create(title=title, text=text, user=request.user, product=product)

    return render(request, 'product/product-details.html', {'product': product})


class ProductList(ListView):
    template_name = 'product/shop_list.html'
    queryset = Product.objects.all()
    paginate_by = 3
    context_object_name = 'product_list'

    def get_context_data(self, **kwargs):
        request = self.request
        caffeine = request.GET.getlist('caffeine')
        category = request.GET.getlist('category')
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        queryset = Product.objects.all()
        print(caffeine, category, min_price, max_price)

        if caffeine:
            queryset = queryset.filter(amountcaffeine__title__in=caffeine).distinct()
        if category:
            queryset = queryset.filter(category__title__in=category).distinct()

        if min_price and max_price:
            queryset = queryset.filter(price__lte=max_price, price__gte=min_price)

        context = super(ProductList, self).get_context_data()
        context['product_list'] = queryset
        return context


def searchbar(request):
    search = request.GET.get('search')
    product_list = Product.objects.filter(title__icontains=search)
    return render(request, 'product/shop_list.html', {'product_list': product_list})
