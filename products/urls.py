
from django.urls import path
from .views import *


urlpatterns = [
    path('', all_products_page, name='all_products'),
    path('<int:pk>', product, name='product')
]