from django.shortcuts import render
from .models import Event, Tournament, TournamentGame, Bonus
from django.db.models import Q

def index(request):
    events = Event.objects.all()
    return render(request, 'index.html', {'events': events})

def cybersport(request):
    tournaments = Tournament.objects.all()
    tournamentGames = TournamentGame.objects.all()
    tournament_search = request.GET.get('search', '')
    if tournament_search:
        tournaments = tournaments.filter(
            Q(name__icontains=tournament_search)
        )
    return render(request, 'cybersport.html', {'tournaments': tournaments, 'tournamentGames': tournamentGames, 'tournament_search': tournament_search})

def bonus(request):
    bonuses = Bonus.objects.all()
    type_filter = request.GET.get('type', '')
    if type_filter:
        bonuses = bonuses.filter(type__icontains=type_filter)
    return render(request, 'bonus.html', {'bonuses': bonuses})