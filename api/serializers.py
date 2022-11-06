from .models import MealModel,RateModel
from rest_framework import serializers

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealModel
        fields = ['id','title','description']

class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateModel
        fields = ['id','stars','meal','user']