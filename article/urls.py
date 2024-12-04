from django.urls import path
from .views import articledetail, ArticleList

app_name = 'article'
urlpatterns = [
    path('detail/<int:pk>', articledetail,name='detail'),
    path('list', ArticleList.as_view(),name='article_list'),
]