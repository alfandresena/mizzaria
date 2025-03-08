from django.urls import path
from . import views

urlpatterns = [
    path('create-order/', views.create_pizza_order, name='create_pizza_order'),
]