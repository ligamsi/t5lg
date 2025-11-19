from django.db import models
from django.utils.text import slugify

class League(models.Model):
    name = models.CharField(max_length=100)

    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class TeamInLeague(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    league = models.ForeignKey(League, on_delete=models.CASCADE)

    matches = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    loses = models.IntegerField(default=0)
    goals_scored = models.IntegerField(default=0)
    goals_conceded = models.IntegerField(default=0)
    difference = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    class Meta:
        unique_together = ('team', 'league')

    def __str__(self):
        return f"{self.team.name} — {self.league.name}"
    
class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name} {self.surname}"
    
class PlayerInLeague(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    league = models.ForeignKey(League, on_delete=models.CASCADE)

    matches = models.IntegerField(default=0)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)

    class Meta:
        unique_together = ('player', 'league')

    def __str__(self):
        return f"{self.player} — {self.league.name}"
    
    