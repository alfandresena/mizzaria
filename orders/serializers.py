from rest_framework import serializers
from .models import Product, Ingredient, Cart, Order, OrderItem

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    produit = ProductSerializer()

    class Meta:
        model = Cart
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    def get_items(self, obj):
        return OrderItemSerializer(obj.items.all(), many=True).data



class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()  # Inclure les détails du produit
    
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']
