from django.shortcuts import render, get_object_or_404, redirect
from account.models import Address, User
from cart.models import Order
from cart.models import OrderItem
from product.models import Product, Like
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from .forms import TicketForm, TicketReplyForm, TicketStatusForm
from .models import Ticket, TicketReply


@login_required
def dashboard(request):
    if request.user.is_authenticated:
        # orders
        delivered = Order.objects.filter(user=request.user, status='Delivered')
        other_order = Order.objects.filter(user=request.user).exclude(status='Delivered')
        # address
        address = Address.objects.all()
        # favorite product
        favorite = request.user.like.values_list('product', flat=True)
        product = Product.objects.filter(id__in=favorite)[:3]
    return render(request, 'dashboard/dashboard.html',
                  {'delivered': delivered, 'other_order': other_order, 'address': address, 'product': product})


@login_required
def dashboard_orders(request):
    if request.user.is_authenticated:
        delivered = Order.objects.filter(user=request.user, status='Delivered').order_by('-created_at')
        other_order = Order.objects.filter(user=request.user).exclude(status='Delivered').order_by('created_at')
        order_item = OrderItem.objects.all()
    return render(request, 'dashboard/dashboard_orders.html',
                  {'delivered': delivered, 'other_order': other_order, 'order_item': order_item})


@login_required
def dashboard_address(request):
    address = Address.objects.all()
    return render(request, 'dashboard/dashboard-address.html', {'address': address})


@login_required
def dashboard_detail_order(request, pk):
    if request.user.is_authenticated:
        order = Order.objects.get(id=pk)
        item = OrderItem.objects.filter(order=pk)
        return render(request, 'dashboard/dashboard_detail_orders.html', {'order': order, 'item': item})


@login_required
def dashboard_favorite(request):
    favorite = request.user.like.values_list('product', flat=True)
    product = Product.objects.filter(id__in=favorite)
    return render(request, 'dashboard/dashboard-favorite.html', {'product': product})


@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('dashboard:ticket_list')
        else:
            return render(request, 'dashboard/dashboard_ticket.html', {'form': form})
    else:
        form = TicketForm
        return render(request, 'dashboard/dashboard_ticket.html', {'form': form})


@login_required
def ticket_list(request):
    tickets = Ticket.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'dashboard/dashboard_ticket_list.html', {'tickets': tickets})


# def ticket_detail(request, pk):
#     if request.user.is_staff:
#         ticket = get_object_or_404(Ticket, pk=pk)
#     else:
#         ticket = get_object_or_404(Ticket, user=request.user, pk=pk)
#
#     if request.method == 'POST':
#         form = TicketReplyForm(request.POST)
#         if form.is_valid():
#             reply = form.save(commit=False)
#             reply.ticket = ticket
#             reply.user = request.user
#             reply.save()
#             return redirect('dashboard:ticket_detail', pk=ticket.id)
#         else:
#             form = TicketReplyForm()
#         return render(request, 'dashboard/dashboard_ticket_detail.html', {'ticket': ticket, 'form': form})

# dashboard/views.py


@login_required
def ticket_detail(request, pk):
    if request.user.is_staff:
        ticket = get_object_or_404(Ticket, pk=pk)
    else:
        ticket = get_object_or_404(Ticket, pk=pk, user=request.user)

    reply_form = TicketReplyForm()
    status_form = TicketStatusForm(instance=ticket) if request.user.is_staff else None

    if request.method == 'POST':
        if 'reply' in request.POST:
            reply_form = TicketReplyForm(request.POST)
            if reply_form.is_valid():
                reply = reply_form.save(commit=False)
                reply.ticket = ticket
                reply.user = request.user
                reply.save()
                return redirect('dashboard:ticket_detail', pk=ticket.pk)

        elif 'status' in request.POST and request.user.is_staff:
            status_form = TicketStatusForm(request.POST, instance=ticket)
            if status_form.is_valid():
                status_form.save()
                return redirect('dashboard:ticket_detail', pk=ticket.pk)

    return render(request, 'dashboard/dashboard_ticket_detail.html', {
        'ticket': ticket,
        'reply_form': reply_form,
        'status_form': status_form,
    })