from django.db import models

# Create your models here.
class PizzaOrder(models.Model):
    user_request = models.CharField(max_length=512)
    response_message = models.TextField(null=True, blank=True)
    options = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"Demande: {self.user_request}"