import random
from typing import List, Dict, Any, Optional
from django.http import JsonResponse


class AIService:
    """
    Service simulant les fonctionnalités d'IA pour l'application de pizza.
    Dans un environnement de production, cette classe interagirait avec un véritable service d'IA.
    """

    @staticmethod
    def get_top_searches() -> Dict[str, List[str]]:
        """Retourne les suggestions de recherche populaires."""
        return {
            "pizza": ["Margherita", "Quatre Fromages", "Pepperoni", "Végétarienne", "Hawaienne"],
            "ingredients": ["Tomate", "Mozzarella", "Jambon", "Champignons", "Olives"],
            "lieu": ["Paris", "Lyon", "Marseille", "Toulouse", "Nice"],
            "autre": ["Pizza pas cher", "Pizza livraison rapide", "Meilleure pizza", "Pizza à emporter"]
        }
    
    @staticmethod
    def search(label: str, localisation: Optional[str] = None, beer_token: Optional[str] = None) -> JsonResponse:
        """Simule une recherche basée sur les critères fournis."""
        # Génération aléatoire de résultats (dans un système réel, cela serait basé sur l'IA)
        pizzas = []
        pizzerias = []
        
        # Création de 5 pizzas aléatoires
        for i in range(1, 6):
            pizzas.append({
                "nom": f"Pizza {label} {i}",
                "image": f"https://example.com/pizza{i}.jpg",
                "localisation": f"Pizzeria {random.choice(['Napoli', 'Roma', 'Milano', 'Venezia'])}",
                "rating": round(random.uniform(3.0, 5.0), 1),
                "nombre_personne_ayant_noter": random.randint(10, 500)
            })
        
        # Création de 3 pizzerias aléatoires
        for i in range(1, 4):
            pizzerias.append({
                "nom": f"Pizzeria {random.choice(['Napoli', 'Roma', 'Milano', 'Venezia'])} {i}",
                "image": f"https://example.com/pizzeria{i}.jpg",
                "localisation": localisation if localisation else f"Ville {random.choice(['Paris', 'Lyon', 'Marseille'])}",
                "is_open": random.choice([True, False])
            })
        
        return {
            "pizza": pizzas,
            "pizzeria": pizzerias
        }
    
    @staticmethod
    def get_menu(pizzeria_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Retourne le menu d'une pizzeria."""
        menu = []
        
        # Création d'un menu aléatoire avec 8 pizzas
        for i in range(1, 9):
            menu.append({
                "nom": f"Pizza {random.choice(['Margherita', 'Quatre Fromages', 'Pepperoni', 'Calzone', 'Royale'])} #{i}",
                "image": f"https://example.com/pizza{i}.jpg",
                "localisation": pizzeria_data.get("nom", "Pizzeria inconnue"),
                "rating": round(random.uniform(3.0, 5.0), 1),
                "nombre_personne_ayant_noter": random.randint(10, 500)
            })
        
        return menu
    
    @staticmethod
    def get_pizza_details(pizza_data: Dict[str, Any]) -> JsonResponse:
        """Retourne les détails d'une pizza."""
        ingredients = []
        
        # Création d'ingrédients aléatoires
        possible_ingredients = [
            ("Tomate", "tomate.jpg"), ("Mozzarella", "mozzarella.jpg"), 
            ("Jambon", "jambon.jpg"), ("Champignons", "champignons.jpg"),
            ("Olives", "olives.jpg"), ("Basilic", "basilic.jpg"),
            ("Roquette", "roquette.jpg"), ("Parmesan", "parmesan.jpg")
        ]
        
        # Sélection de 3 à 6 ingrédients
        selected_ingredients = random.sample(possible_ingredients, random.randint(3, 6))
        
        for ingredient_name, img in selected_ingredients:
            ingredients.append({
                "nom": ingredient_name,
                "image": f"https://example.com/{img}"
            })
        
        return JsonResponse({
            "nom": pizza_data["nom"],
            "image": pizza_data["image"],
            "localisation": pizza_data["localisation"],
            "rating": pizza_data["rating"],
            "nombre_personne_ayant_noter": pizza_data["nombre_personne_ayant_noter"],
            "prix": round(random.uniform(8.0, 18.0), 2),
            "disponibilite_pm": random.choice([True, False]),
            "disponibilite_gm": random.choice([True, False]),
            "liste_ingredients": ingredients
        })
