from usercakes.models import *
from rest_framework import serializers


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = '__all__'


class PlaceOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'