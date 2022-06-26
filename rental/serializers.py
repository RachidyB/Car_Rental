from rest_framework import serializers
from .models import *


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
    image = serializers.ImageField(max_length=None, allow_empty_file=False, allow_null=False, use_url=True,
                                   required=False)


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
