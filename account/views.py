from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import View
from sqlparse import format

from .forms import LoginForm, RegisterForm, CheckOtpForm, CreateAddress
from .models import Otp
import random
from uuid import uuid4
from django.contrib.auth import get_user_model
from account.models import Address

User = get_user_model()


class Login(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'account/login.html', context={'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['phone'], password=cd['password'])
            if user is not None:
                login(request, user)
                next_page = request.POST.get('next')
                if next_page:
                    return redirect(next_page)
                return redirect('/')
            else:
                form.add_error('phone', 'اطلاعات ورود نامعتبر است')

        return render(request, 'account/login.html', {'form': form})


def signout(request):
    logout(request)
    return redirect('/')


class Signin(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'account/signup.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            rand = random.randint(1000, 9999)
            print(rand)
            # SMS.verification({'receptor': '09xxxxxxxxx', 'type': '1', 'template': 'Your Template', 'param1': 'test'})
            token = str(uuid4())
            Otp.objects.create(phone=cd['phone'], code=rand, token=token)

            return redirect(reverse('account:check') + f'?token={token}')
        else:
            form.add_error('phone', 'invalid user data')
        return render(request, 'account/signup.html', {'form': form})


class CheckOtp(View):
    def get(self, request):
        form = CheckOtpForm()
        return render(request, 'account/checkotp.html', {'form': form})

    def post(self, request):
        token = request.GET.get('token')
        form = CheckOtpForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if Otp.objects.filter(code=cd['code'], token=token).exists():
                otp = Otp.objects.get(token=token)
                user, is_created = User.objects.get_or_create(phone=otp.phone)
                login(request, user)
            return redirect('/')
        else:
            form.add_error('phone', 'invalid user data')

        return render(request, 'account/checkotp.html', {'form': form})


class AddAddress(View):
    def get(self, request):
        form = CreateAddress()
        return render(request, 'account/address.html', {'form': form})

    def post(self, request):
        form = CreateAddress(request.POST)

        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            next_page = request.GET.get('next')
            if next_page:
                return redirect(next_page)
        return render(request, 'dashboard/dashboard.html')


def edit_address(request, pk):
    form = CreateAddress()
    address = get_object_or_404(Address, pk=pk, user=request.user)
    if request.method == 'POST':
        form = CreateAddress(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return redirect('dashboard:dashboard_address')
        else:
            form = CreateAddress(request.POST, instance=address)
    return render(request, 'account/edit_address.html', {'form': form})


def delete_address(request, pk):
    address = get_object_or_404(Address, user=request.user, pk=pk)
    address.delete()
    return redirect('dashboard:dashboard_address')


