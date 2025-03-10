from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    """ Table pour stocker les pizzas """
    nom = models.CharField(max_length=255)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    localisation = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    taille = models.CharField(max_length=2, choices=[('pm', 'PM'), ('gm', 'GM')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom

class Ingredient(models.Model):
    """ Table pour stocker les ingrédients des pizzas """
    nom = models.CharField(max_length=255)
    image = models.ImageField(upload_to="ingredients/", blank=True, null=True)
    produits = models.ManyToManyField(Product, related_name="ingredients")

    def __str__(self):
        return self.nom

class Cart(models.Model):
    """ Table pour stocker les produits du panier d'un utilisateur """
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    produit = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    date_livraison = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    """ Table pour stocker les commandes passées par un utilisateur """
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    statut = models.CharField(max_length=20, choices=[('en cours', 'En cours'), ('livré', 'Livré')], default='en cours')
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    """ Détail des produits commandés dans une commande """
    commande = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    produit = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
