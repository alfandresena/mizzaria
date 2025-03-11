from django.urls import path
from .views import top_search, menu, details, search

urlpatterns = [
    path('topSearch/', top_search, name='top_search'),
    path('search/', search, name='search'),
    path('menu/', menu, name='menu'),
    path('details/', details, name='details'),
]
