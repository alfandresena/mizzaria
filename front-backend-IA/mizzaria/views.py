from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # Vous devez créer ce template HTML
