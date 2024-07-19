from rest_framework import viewsets
from .models import OnePieceCard, FusionWorldCard
from .serializers import OnePieceCardSerializer, FusionWorldCardSerializer

class OnePieceCardViewSet(viewsets.ModelViewSet):
    queryset = OnePieceCard.objects.all()
    serializer_class = OnePieceCardSerializer

class FusionWorldCardViewSet(viewsets.ModelViewSet):
    queryset = FusionWorldCard.objects.all()
    serializer_class = FusionWorldCardSerializer
