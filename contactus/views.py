from django.shortcuts import render

from contactus.forms import MessageForm


def contactview(request):
    if request.method == 'POST':
        contact = MessageForm(data=request.POST)

        if contact.is_valid():
            contact.save()
    else:
        contact = MessageForm()

    return render(request, 'contact/contact-us.html', context={'contact': contact})


def question(request):
    return render(request, 'contact/questions.html')


def aboutus(request):
    return render(request, 'contact/aboute-us.html')
