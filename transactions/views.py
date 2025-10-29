from django.db.models import Sum, F, DecimalField, ExpressionWrapper, Q
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, permissions

from .models import Transaction
from .serializers import TransactionSerializer
from portfolios.permissions import IsOwnerOrReadOnly


class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Transaction.objects.filter(asset__portfolio__user=self.request.user)

    def perform_create(self, serializer):
        transaction = serializer.save()
        asset = transaction.asset

        if transaction.transaction_type == 'buy':
            asset.quantity += transaction.quantity
        elif transaction.transaction_type == 'sell':
            asset.quantity -= transaction.quantity
        asset.save()

    # ✅ Endpoint corregido
    @action(detail=False, methods=['get'], url_path='summary/(?P<portfolio_id>[^/.]+)')
    def portfolio_summary(self, request, portfolio_id=None):
        qs = Transaction.objects.filter(
            asset__portfolio__id=portfolio_id,
            asset__portfolio__user=request.user
        )

        summary = qs.values('asset__symbol').annotate(
            total_bought=Sum(
                ExpressionWrapper(
                    F('quantity') * F('price'),
                    output_field=DecimalField(max_digits=20, decimal_places=2)
                ),
                filter=Q(transaction_type='buy')
            ),
            total_sold=Sum(
                ExpressionWrapper(
                    F('quantity') * F('price'),
                    output_field=DecimalField(max_digits=20, decimal_places=2)
                ),
                filter=Q(transaction_type='sell')
            ),
            total_quantity=Sum(
                F('quantity'),
                filter=Q(transaction_type='buy')
            ) - Sum(
                F('quantity'),
                filter=Q(transaction_type='sell')
            )
        )

        return Response(summary)
