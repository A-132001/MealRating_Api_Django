from django.shortcuts import render
from .models import RateModel,MealModel
from rest_framework import viewsets
from .serializers import MealSerializer,RateSerializer

class MealViewset(viewsets.ModelViewSet):
    queryset = MealModel.objects.all()
    serializer_class = MealSerializer

class RateViewset(viewsets.ModelViewSet):
    queryset = RateModel.objects.all()
    serializer_class = RateSerializer

