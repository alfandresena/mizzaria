from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils.auto_completion import combined_suggestions

@csrf_exempt
def auto_completion(request):
    if request.method == 'GET':
        prompt = request.GET.get('prompt', '')
        suggestions = combined_suggestions(prompt, limit=5, score_min=30)
        return JsonResponse({'suggestions': suggestions})
    return JsonResponse({'error': 'Méthode non autorisée'}, status=405)