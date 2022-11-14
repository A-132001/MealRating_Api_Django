from .models import MealModel,RateModel
from rest_framework import serializers
from django.contrib.auth.models import User
class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealModel
        fields = ['id','title','description','num_of_rating_on_meal','avg_of_stars']

class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateModel
        fields = ['id','stars','meal','user']
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","password",'email']
        
        extra_kwargs = {'password':{'write_only':True,'required':True}}