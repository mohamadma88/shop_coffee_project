from django.urls import path
from .views import CartView, AddCart,CartDelete ,OrderDetail , OrderCreation

app_name = 'cart'
urlpatterns = [
    path('cart', CartView.as_view(), name='cart'),
    path('add/<int:pk>', AddCart.as_view(), name='add_cart'),
    path('delete/<str:id>', CartDelete.as_view(), name='delete'),
    path('order/<int:pk>', OrderDetail.as_view(), name='order'),
    path('order/create', OrderCreation.as_view(), name='order_create'),

]
