from django.urls import path
from .views import dashboard, dashboard_orders, dashboard_address, dashboard_detail_order, dashboard_favorite, \
    create_ticket, ticket_list , ticket_detail

app_name = 'dashboard'
urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('orders', dashboard_orders, name='orders'),
    path('address', dashboard_address, name='address'),
    path('order/detail/<int:pk>', dashboard_detail_order, name='detail_order'),
    path('favorite', dashboard_favorite, name='favorite'),
    path('ticket/', create_ticket, name='ticket'),
    path('ticket/list', ticket_list, name='ticket_list'),
    path('ticket/detail/<int:pk>', ticket_detail, name='ticket_detail'),

]
