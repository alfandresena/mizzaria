from django.shortcuts import render
from rest_framework import status
from rest_framework import Response
from rest_framework.decorators import api_view
from .models import PizzaOrder
from .serializers import PizzaOrderSerializer
from .solona_IA import get_ai_response

# une vue pour recevoir les demandes de l'utilisateur et interagir avec l'IA dans pizza_order/views.py..

@api_view(['POST'])
def create_pizza_order(request):
    if request.method == 'POST':
        user_request = request.data.get('user_request', None)
        if not user_request:
            return Response({"error": "La demande de l'utilisateur est requise."}, status=status.HTTP_400_BAD_REQUEST)

        # Appeler le script IA pour obtenir la reponse
        response_message, options = get_ai_response(user_request)

        #Creer un nouvel ordre de pizza avec la reponse de l'IA
        pizza_order = PizzaOrder.objects.create(
            user_request=user_request,
            response_message=response_message,
            options=options
        )

        #Serialiser et renvoyer la reponse
        serializer = PizzaOrderSerializer(pizza_order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)