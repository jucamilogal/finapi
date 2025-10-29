from rest_framework import serializers
from .models import Asset

class AssetSerializer(serializers.ModelSerializer):
    total_value = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = Asset
        fields = [
            'id', 'portfolio', 'symbol', 'name', 'asset_type',
            'price', 'quantity', 'total_value', 'added_at'
        ]
        read_only_fields = ['id', 'added_at', 'total_value']

    def validate_symbol(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("El símbolo debe tener al menos 2 caracteres.")
        return value
