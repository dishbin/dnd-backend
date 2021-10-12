from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=50)
    character_class = models.CharField(max_length=50)
    HP = models.IntegerField()
    damage_die = models.CharField(max_length=10)
    coin = models.IntegerField()
    STR = models.IntegerField()
    DEX = models.IntegerField()
    CON = models.IntegerField()
    INT = models.IntegerField()
    WIS = models.IntegerField()
    CHA = models.IntegerField()
    equipment = models.TextField()
    spells = models.TextField()

    def __str__(self):
        return self.name

