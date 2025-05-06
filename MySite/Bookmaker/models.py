from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    ratio1 = models.DecimalField(max_digits=5, decimal_places=2)
    tie = models.DecimalField(max_digits=5, decimal_places=2)
    ratio2 = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class Tournament(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class TournamentGame(models.Model):
    name = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    ratio1 = models.DecimalField(max_digits=5, decimal_places=2)
    ratio2 = models.DecimalField(max_digits=5, decimal_places=2)
    tournament = models.IntegerField()


    def __str__(self):
        return self.name

class Bonus(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)


    def __str__(self):
        return self.name