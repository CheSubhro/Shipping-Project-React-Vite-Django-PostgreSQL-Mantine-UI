
from rest_framework import serializers
from .models import ShippingRate

class ShippingCalculationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingRate
        fields = ['source_city', 'destination_city', 'distance_km', 'weight_kg', 'total_cost']
        read_only_fields = ['total_cost'] 