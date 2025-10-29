from rest_framework import serializers
from .models import Portfolio

class PortfolioSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Portfolio
        fields = ['id', 'name', 'base_currency', 'description', 'created_at', 'user']
        read_only_fields = ['id', 'created_at', 'user']

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("El nombre del portafolio debe tener al menos 3 caracteres.")
        return value
