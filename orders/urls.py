from django.urls import path
from .views import AddPizzaToCart, DeletePizzaFromCart, UpdatePizzaFromCart, ReadCart, OrderView, ReadOrder

urlpatterns = [
    path('add_pizza_to_card/', AddPizzaToCart.as_view(), name="add_pizza"),
    path('delete_pizza_from_card/', DeletePizzaFromCart.as_view(), name="delete_pizza"),
    path('update_pizza_from_card/', UpdatePizzaFromCart.as_view(), name="update_pizza"),
    path('read_card/', ReadCart.as_view(), name="read_cart"),
    path('order/', OrderView.as_view(), name="order"),
    path('read_order/', ReadOrder.as_view(), name="read_order"),
]
