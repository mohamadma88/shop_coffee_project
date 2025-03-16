from django.shortcuts import render


def home(request):
    return render(request, 'home/index.html')


def page_404(request,exception):
    return render(request, 'home/404.html')
