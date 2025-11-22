from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import League, TeamInLeague, PlayerInLeague

def main_page(request):
    leagues = League.objects.all()

    # получаем slug выбранной лиги
    selected_slug = request.GET.get("league")

    # если ничего не выбрано — берём первую лигу
    if selected_slug:
        league = get_object_or_404(League, slug=selected_slug)
    else:
        league = leagues.first()

    teams = TeamInLeague.objects.filter(league=league).order_by('-points', '-difference', '-goals_scored')
    players = PlayerInLeague.objects.filter(league=league).order_by('-goals')

    return render(request, "main_page.html", {
        "leagues": leagues,
        "league": league,
        "teams": teams,
        "players": players,
    })
