# from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('create', create_news, name='create_news'),
    path('', all_news, name='all_news'),
    path('<int:pk>', one_new, name='one_new'),
    path('en', en_all_news, name='en_all_news'),
    path('<int:pk>/en', en_one_new, name='en_one_new'),
]