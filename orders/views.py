from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from .models import Produit, Panier, PanierProduit, Commande, CommandeProduit
from .serializers import ProduitSerializer, PanierSerializer, CommandeSerializer

class PanierViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def add_pizza_to_card(self, request):
        user = request.user
        data = request.data

        produit, created = Produit.objects.get_or_create(
            nom=data['nom'], localisation=data['localisation'],
            image=data.get('image', ''), prix=data['prix'], taille=data['taille']
        )

        panier, _ = Panier.objects.get_or_create(utilisateur=user)

        panier_produit, created = PanierProduit.objects.get_or_create(
            panier=panier, produit=produit
        )
        panier_produit.quantite = data['quantite']
        panier_produit.save()

        return Response({"status": True}, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def delete_pizza_from_card(self, request):
        user = request.user
        data = request.data

        produit = Produit.objects.filter(
            nom=data['nom'], localisation=data['localisation'], prix=data['prix'], taille=data['taille']
        ).first()

        if produit:
            PanierProduit.objects.filter(panier__utilisateur=user, produit=produit).delete()

        return Response({"status": True})

    @action(detail=False, methods=['post'])
    def update_pizza_from_card(self, request):
        user = request.user
        data = request.data

        produit = Produit.objects.filter(
            nom=data['nom'], localisation=data['localisation'], prix=data['prix'], taille=data['taille']
        ).first()

        if produit:
            panier_produit = PanierProduit.objects.filter(panier__utilisateur=user, produit=produit).first()
            if panier_produit:
                panier_produit.quantite = data['quantite']
                panier_produit.save()

        return Response({"status": True})

    @action(detail=False, methods=['get'])
    def read_card(self, request):
        user = request.user
        panier = Panier.objects.filter(utilisateur=user).first()
        serializer = PanierSerializer(panier)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def order(self, request):
        user = request.user
        panier = Panier.objects.filter(utilisateur=user).first()
        if panier:
            commande = Commande.objects.create(utilisateur=user)

            for panier_produit in PanierProduit.objects.filter(panier=panier):
                CommandeProduit.objects.create(
                    commande=commande, produit=panier_produit.produit, quantite=panier_produit.quantite
                )
            
            PanierProduit.objects.filter(panier=panier).delete()

        return Response({"status": True})

    @action(detail=False, methods=['post'])
    def read_order(self, request):
        user = request.user
        commandes = Commande.objects.filter(utilisateur=user)
        serializer = CommandeSerializer(commandes, many=True)
        return Response(serializer.data)

