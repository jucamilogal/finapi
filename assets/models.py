from django.db import models
from portfolios.models import Portfolio

class Asset(models.Model):
    ASSET_TYPES = [
        ('stock', 'Stock'),
        ('crypto', 'Cryptocurrency'),
        ('etf', 'ETF'),
        ('bond', 'Bond'),
    ]

    portfolio = models.ForeignKey(
        Portfolio, on_delete=models.CASCADE, related_name='assets'
    )
    symbol = models.CharField(max_length=10)              # Ej: AAPL, BTC
    name = models.CharField(max_length=100)               # Ej: Apple Inc., Bitcoin
    asset_type = models.CharField(max_length=10, choices=ASSET_TYPES)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    quantity = models.DecimalField(max_digits=15, decimal_places=4, default=0)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('portfolio', 'symbol')
        ordering = ['-added_at']

    def __str__(self):
        return f"{self.symbol} - {self.portfolio.name}"

    @property
    def total_value(self):
        return self.price * self.quantity
