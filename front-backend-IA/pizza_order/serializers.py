from rest_framework import serializers
from .models import PizzaOrder

# un serializer pour gérer la sérialisation des données dans pizza_order/serializers.py.

class PizzaOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaOrder
        fields = ['user_request', 'response_message', 'options']
