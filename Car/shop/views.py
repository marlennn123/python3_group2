from rest_framework import viewsets, permissions
from .models import *
from .permissions import IsOwnerOrReadOnly
from .serializers import *


class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = Category
    permission_classes = [permissions.IsAdminUser]


class CarViewSets(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = Car
    permission_classes = [permissions.IsAdminUser]

class BetViewSets(viewsets.ModelViewSet):
    queryset = Bet.objects.all()
    serializer_class = Bet
    permission_classes = [permissions.IsAdminUser]