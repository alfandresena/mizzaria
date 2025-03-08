from rest_framework import serializers
from .models import PizzaOrder

class PizzaOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaOrder
        fields = ['user_request', 'response_message', 'options']
