from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Article


def articledetail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article/article-details.html', {'article': article})


class ArticleList(ListView):
    template_name = 'article/articles.html'
    queryset = Article.objects.all()
    paginate_by = 3
    context_object_name = 'article_list'

    # def get_context_data(self, **kwargs):
    #     request = self.request
    #
    #     category = request.GET.getlist('category')
    #
    #     queryset = Article.objects.all()
    #     print(category)
    #     if category:
    #         queryset = queryset.filter(category__title__in=category).distinct()
    #
    #     context = super(ArticleList, self).get_context_data()
    #     context['article_list'] = queryset
    #     return context
