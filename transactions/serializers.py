from rest_framework import serializers
from .models import Transaction
from assets.models import Asset

class TransactionSerializer(serializers.ModelSerializer):
    total_value = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)
    asset_name = serializers.ReadOnlyField(source='asset.name')
    portfolio_id = serializers.ReadOnlyField(source='asset.portfolio.id')

    class Meta:
        model = Transaction
        fields = [
            'id', 'asset', 'asset_name', 'portfolio_id',
            'transaction_type', 'quantity', 'price',
            'total_value', 'date'
        ]
        read_only_fields = ['id', 'date', 'total_value', 'asset_name', 'portfolio_id']

    def validate(self, data):
        asset = data.get('asset')
        quantity = data.get('quantity')
        transaction_type = data.get('transaction_type')

        # No permitir venta de más cantidad que la disponible
        if transaction_type == 'sell' and quantity > asset.quantity:
            raise serializers.ValidationError(f"No puedes vender más ({quantity}) de lo que posees ({asset.quantity}).")
        return data
