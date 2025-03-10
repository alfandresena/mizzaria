from django.contrib import admin

# Register your models here.
from .models import Product, Ingredient, Cart, Order, OrderItem

admin.site.register(Product)
admin.site.register(Ingredient)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)
