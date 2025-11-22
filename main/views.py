from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import League, TeamInLeague, PlayerInLeague

def main_page(request):
    league_slug = request.GET.get("league")

    # Получаем все лиги
    leagues = League.objects.all()

    # По умолчанию берём первую лигу
    current_league = None
    if league_slug:
        current_league = League.objects.filter(slug=league_slug).first()
    if not current_league:
        current_league = leagues.first()

    # Таблица
    table = TeamInLeague.objects.filter(league=current_league)

    # Статистика игроков
    players_stats = PlayerInLeague.objects.filter(league=current_league)

    return render(request, "main_page.html", {
        "leagues": leagues,
        "current_league": current_league,
        "table": table,
        "players_stats": players_stats,
    })
