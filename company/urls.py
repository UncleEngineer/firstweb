from django.urls import path
from .views import Homepage, about, product

urlpatterns = [
    path('', Homepage), # localhost:8000
    path('about', about),
    path('product', product),
]