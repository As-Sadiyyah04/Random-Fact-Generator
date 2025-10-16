from django.urls import path
from . import views

urlpatterns = [
    path('random/', views.random_fact_view, name='random_fact'),
    path('search/', views.search_facts_view, name='search_facts'),
]