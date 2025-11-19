from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import League, TeamInLeague, PlayerInLeague

def league_list(request):
    leagues = League.objects.all()
    return render(request, 'main/league_list.html', {'leagues': leagues})


def league_table(request, league_slug):
    league = get_object_or_404(League, slug=league_slug)
    table = TeamInLeague.objects.filter(league=league).order_by('-points', '-difference')
    return render(request, 'main/league_table.html', {
        'league': league,
        'table': table
    })


def league_players(request, league_slug):
    league = get_object_or_404(League, slug=league_slug)
    players = PlayerInLeague.objects.filter(league=league).order_by('-goals', '-assists')
    return render(request, 'main/league_players.html', {
        'league': league,
        'players': players
    })
# Create your views here.
