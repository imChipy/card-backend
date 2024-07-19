from django.db import models

class OnePieceCard(models.Model):
    key = models.CharField(max_length=10, unique=True )
    card_id = models.CharField(max_length=10, default='N/A')
    rarity = models.CharField(max_length=10, default='N/A')
    category = models.CharField(max_length=50, default='N/A')
    card_name = models.CharField(max_length=100, default='N/A')
    cost = models.IntegerField(default=-999)
    power = models.IntegerField(default=-999)
    counter = models.IntegerField(default=-999)
    color = models.CharField(max_length=50, default='N/A')
    type = models.JSONField(default=list)
    effect = models.TextField(default='N/A')
    art = models.IntegerField(default=-999)
    trigger = models.CharField(max_length=100, default='N/A')
    card_set = models.CharField(max_length=100, default='N/A')
    image = models.ImageField(upload_to='one_piece_cards/', null=True, blank=True)

    def __str__(self):
        return self.card_name

class FusionWorldCard(models.Model):
    key = models.CharField(max_length=10, unique=True)
    export = models.IntegerField(default=-999)
    card_id = models.JSONField(default=list)
    rarity = models.CharField(max_length=10, default='N/A')
    category = models.CharField(max_length=50, default='N/A')
    card_name = models.CharField(max_length=100, default='N/A')
    cost = models.JSONField(default=dict)
    power = models.IntegerField(default=-999)
    counter = models.IntegerField(default=-999)
    color = models.JSONField(default=list)
    type = models.JSONField(default=list)
    effect = models.TextField(default='N/A')
    art = models.IntegerField(default=-999)
    trigger = models.CharField(max_length=100, default='N/A')
    card_set = models.CharField(max_length=100, default='N/A')
    image = models.ImageField(upload_to='fusion_world_cards/', null=True, blank=True)

    def __str__(self):
        return self.card_name

