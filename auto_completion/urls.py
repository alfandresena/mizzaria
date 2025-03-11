from django.urls import path
from .views import auto_completion

urlpatterns = [
    path('auto-completion/', auto_completion, name='auto_completion'),
]