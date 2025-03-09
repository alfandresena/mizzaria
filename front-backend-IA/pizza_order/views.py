from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import PizzaOrder
from .serializers import PizzaOrderSerializer
from .solona_IA import get_ai_response

@api_view(['POST'])
def create_pizza_order(request):
    if request.method == 'POST':
        user_request = request.data.get('user_request', None)
        if not user_request:
            return Response({"error": "La demande de l'utilisateur est requise."}, status=status.HTTP_400_BAD_REQUEST)

        # Obtenir la réponse de l'IA
        response_message = get_ai_response(user_request)
        print("✅ Réponse trouvée :", response_message)

        # Créer un nouvel ordre de pizza avec la réponse de l'IA
        pizza_order = PizzaOrder.objects.create(
            user_request=user_request,
            response_message=response_message,
        )

        # Serialiser et renvoyer la réponse
        serializer = PizzaOrderSerializer(pizza_order)
        return Response({
            'response_message': response_message,  # Transmettre la réponse au front
        }, status=status.HTTP_201_CREATED)
