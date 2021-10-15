from django.shortcuts import render

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from oxyenny_site.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL


def homepage(request):
    return render(request, 'homepage.html')


def contact_view(request):
    # если метод GET, вернем форму
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST['name']
        phone = request.POST['phone']
        from_email = request.POST['form_email']
        message = request.POST['message']
        try:
            send_mail(f'Buy yacht from {name}, {from_email}, {phone}', message,
                      DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
        except BadHeaderError:
            return HttpResponse('Ошибка в теме письма.')
        return redirect('homepage')

    return render(request, "email.html")


def success_view(request):
    return HttpResponse('Приняли! Спасибо за вашу заявку.')
