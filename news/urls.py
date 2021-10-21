# from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('create', create_news, name='create_news'),
    # path('', contact_view, name='contact'),
    # path('success', success_view, name='success')
]