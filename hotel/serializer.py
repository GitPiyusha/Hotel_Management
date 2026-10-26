
from rest_framework import serializers

from hotel.models import HotelModel


class HotelSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=10)
    address = serializers.CharField(max_length=100)
    rating = serializers.IntegerField()

    class Meta:
        model = HotelModel
        fields = '__all__'