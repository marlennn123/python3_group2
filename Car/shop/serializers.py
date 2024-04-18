from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'



class BetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bet
        fields = '__all__'
