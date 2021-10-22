from django.shortcuts import render, redirect
from .forms import *
from news.models import *
from django.db import transaction


@transaction.atomic
def create_news(request):
    if request.user.is_superuser:
        if request.method == 'GET':
            return render(request, 'create_news.html', {'form': NewsForm()})
        else:
            form = NewsForm(request.POST, request.FILES)
            if form.is_valid():
                news = News(ru_title=form.cleaned_data['ru_title'],
                            en_title=form.cleaned_data['en_title'],
                            ru_text=form.cleaned_data['ru_text'],
                            en_text=form.cleaned_data['en_text'],
                            image=request.FILES['media'])
                news.save()
                return redirect('homepage')
            print(form.errors)
    else:
        redirect('homepage')


def all_news(request):
    return render(request, 'all_news.html', {'news': News.objects.all()})


def one_new(request, pk):
    return render(request, 'new.html', {'new': News.objects.get(pk=pk)})
