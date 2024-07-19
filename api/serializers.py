from rest_framework import serializers
from .models import OnePieceCard, FusionWorldCard

class OnePieceCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnePieceCard
        fields = '__all__'

class FusionWorldCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = FusionWorldCard
        fields = '__all__'
