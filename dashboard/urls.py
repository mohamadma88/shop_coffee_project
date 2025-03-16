from django.urls import path
from .views import dashboard, dashboard_orders, dashboard_address, dashboard_detail_order, dashboard_favorite

app_name = 'dashboard'
urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('orders', dashboard_orders, name='orders'),
    path('address', dashboard_address, name='address'),
    path('order/detail/<int:pk>', dashboard_detail_order, name='detail_order'),
    path('favorite', dashboard_favorite, name='favorite'),

]
