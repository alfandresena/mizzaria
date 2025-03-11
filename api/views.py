from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .ai_service import AIService

# Vue pour obtenir les suggestions de recherche les plus populaires
@api_view(['GET'])
def top_search(request):
    """Endpoint pour obtenir les suggestions de recherche les plus populaires."""
    suggestions = AIService.get_top_searches() 
    return JsonResponse(suggestions)  # Réponse en JSON

# Vue pour effectuer une recherche basée sur les entrées utilisateur
@api_view(['POST'])
def search(request):
    """Endpoint de recherche basé sur les entrées utilisateur."""
    label = request.data.get('label', '')
    localisation = request.data.get('localisation', None)
    beer_token = request.data.get('beer-token', None)
    
    # Appel au service IA pour effectuer la recherche
    search_results = AIService.search(label, localisation, beer_token)

    # Enregistrer la recherche dans l'historique si l'utilisateur est connecté
    # if request.user.is_authenticated:
    #     SearchHistory.objects.create(
    #         utilisateur=request.user,
    #         beer_token=beer_token,
    #         requete=label
    #     )
    
    return JsonResponse(search_results)  # Réponse en JSON

# Vue pour obtenir le menu d'une pizzeria
@api_view(['POST'])
def menu(request):
    """Endpoint pour obtenir le menu d'une pizzeria."""
    pizzeria_data = request.data
    menu_data = AIService.get_menu(pizzeria_data)
    return Response(menu_data)  # Réponse en JSON

# Vue pour obtenir les détails d'une pizza
@api_view(['POST'])
def details(request):
    """Endpoint pour obtenir les détails d'une pizza."""
    pizza_data = request.data
    details_data = AIService.get_pizza_details(pizza_data)
    return Response(details_data)  # Réponse en JSON
