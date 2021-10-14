# from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('contact', contact_view, name='contact'),
    path('success', success_view, name='success')
]