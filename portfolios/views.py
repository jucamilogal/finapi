from rest_framework import viewsets, permissions
from .models import Portfolio
from .serializers import PortfolioSerializer
from .permissions import IsOwnerOrReadOnly

class PortfolioViewSet(viewsets.ModelViewSet):
    serializer_class = PortfolioSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        # Cada usuario solo ve sus propios portfolios
        return Portfolio.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Asigna automáticamente el usuario autenticado
        serializer.save(user=self.request.user)
