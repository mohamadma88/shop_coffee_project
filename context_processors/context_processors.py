from product.models import Product, Category
from article.models import Article


def recent(request):
    recent_product = Product.objects.all().order_by('-create')[:5]
    recent_article = Article.objects.all().order_by('-created_at')[:4]
    category = Category.objects.all()
    return {'recent_product': recent_product, 'recent_article': recent_article,'category':category}
