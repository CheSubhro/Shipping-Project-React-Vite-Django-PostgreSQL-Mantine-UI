
from django.db import models

class ShippingRate(models.Model):
    source_city = models.CharField(max_length=100)
    destination_city = models.CharField(max_length=100)
    distance_km = models.FloatField()
    weight_kg = models.FloatField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.source_city} to {self.destination_city}"