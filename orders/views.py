from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Product, Cart, Order, OrderItem
from .serializers import CartSerializer, OrderSerializer

class AddPizzaToCart(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Logique pour ajouter une pizza au panier
        return Response({"status": True}, status=status.HTTP_201_CREATED)

class DeletePizzaFromCart(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Logique pour supprimer une pizza du panier
        return Response({"status": True}, status=status.HTTP_200_OK)

class UpdatePizzaFromCart(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Logique pour mettre à jour la quantité
        return Response({"status": True}, status=status.HTTP_200_OK)

class ReadCart(generics.ListAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(utilisateur=self.request.user)

class OrderView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Logique pour valider une commande
        return Response({"status": True}, status=status.HTTP_201_CREATED)

class ReadOrder(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(utilisateur=self.request.user)
