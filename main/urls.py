from django.urls import path
from . import views

urlpatterns = [
    path('', views.league_list, name='league_list'),
    path('<slug:league_slug>/table/', views.league_table, name='league_table'),
    path('<slug:league_slug>/players/', views.league_players, name='league_players'),
]