from django.urls import path
from . import views
from .views import ProductList

app_name = 'product'
urlpatterns = [
    path('detail/<int:pk>', views.detail, name='detail'),
    path('search', views.searchbar, name='search'),
    # path('list', views.productlist, name='list'),
    path('list',ProductList.as_view(),name='list')

]
