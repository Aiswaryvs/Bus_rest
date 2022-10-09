from dataclasses import fields
import email
from pyexpat import model
from rest_framework import serializers
from Bus.models import BusList, Reservation, Price,User



class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusList
        fields = "__all__"


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "name","email","password"
        ]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    class Meta:
        model = User
        fields = ['email','password']

class PriceSerializer(serializers.ModelSerializer):
    bus = BusSerializer(read_only=True)
    class Meta:
        model = Price
        fields = ['price','bus']
