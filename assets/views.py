from rest_framework import viewsets, permissions
from .models import Asset
from .serializers import AssetSerializer
from portfolios.permissions import IsOwnerOrReadOnly

class AssetViewSet(viewsets.ModelViewSet):
    serializer_class = AssetSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        # Solo muestra activos de portfolios pertenecientes al usuario autenticado
        return Asset.objects.filter(portfolio__user=self.request.user)

    def perform_create(self, serializer):
        # Asegura que solo se pueda crear dentro de portfolios del usuario autenticado
        portfolio = serializer.validated_data.get('portfolio')
        if portfolio.user != self.request.user:
            raise PermissionError("No puedes agregar activos a portfolios de otros usuarios.")
        serializer.save()
