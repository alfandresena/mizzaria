from django.db import models

class PizzaOrder(models.Model):
    user_request = models.TextField()
    response_message = models.TextField(default="")  # Valeur par défaut vide
    options = models.JSONField(default=list)  # Valeur par défaut pour éviter NULL

    def __str__(self):
        return f"Commande: {self.user_request}"
