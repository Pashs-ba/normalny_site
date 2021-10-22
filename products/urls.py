
from django.urls import path
from .views import *


urlpatterns = [
    path('', all_products_page, name='all_products'),
    path('<int:pk>', product, name='product'),
    path('en', en_all_products_page, name='en_all_products'),
    path('<int:pk>/en', en_product, name='en_product')
]