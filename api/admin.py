from django.contrib import admin
from .models import OnePieceCard, FusionWorldCard

@admin.register(OnePieceCard)
class OnePieceCardAdmin(admin.ModelAdmin):
    list_display = ('key','card_name', 'cost', 'power', 'type_as_list', 'card_set')
    search_fields = ('card_name',)
    list_filter = ('cost', 'power', 'type', 'card_set')

    def type_as_list(self, obj):
        return ', '.join(obj.type)
    type_as_list.short_description = 'Type'

@admin.register(FusionWorldCard)
class FusionWorldCardAdmin(admin.ModelAdmin):
    list_display = ('key', 'card_id', 'rarity', 'category', 'card_name', 'cost', 'power', 'counter', 'color_as_list', 'type_as_list', 'effect', 'art', 'image') 
    search_fields = ('card_name', 'key', 'category')
    list_filter = ('cost', 'power', 'card_set')

    def color_as_list(self, obj):
        return ', '.join(obj.color)
    color_as_list.short_description = 'Color'

    def type_as_list(self, obj):
        return ', '.join(obj.type)
    type_as_list.short_description = 'Type'
