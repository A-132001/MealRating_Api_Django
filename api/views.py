from django.shortcuts import render
from .models import RateModel,MealModel
from rest_framework import viewsets,status
from .serializers import MealSerializer,RateSerializer,UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authtoken.models import Token
#api/meals/pk/rate_meal
class MealViewset(viewsets.ModelViewSet):
    queryset = MealModel.objects.all()
    serializer_class = MealSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    @action(methods = ['post'],detail=True)
    def rate_meal(self,request,pk=None):
        if 'stars' in request.data:
            meal = MealModel.objects.get(id=pk)
            stars = request.data['stars']
            user  = request.user
            # username = request.data['username']
            # user =  User.objects.get(username= username)
            # update or create ,,,, or mean use try in your code
            try:
                rating = RateModel.objects.get(user=user.id,meal=meal.id)
                rating.stars = stars
                rating.save()
                serializer = RateSerializer(rating,many=False)
                json ={
                    "massage":"Update Successfully",
                    'rating meal':serializer.data
                }
                return  Response(json,status=status.HTTP_200_OK)
            except:
                rating = RateModel.objects.create(user=user,meal=meal,stars=stars)
                serializer = RateSerializer(rating,many=False)
                json ={
                    "massage":"Create Successfully",
                    'Meal rating':serializer.data
                }
                return  Response(json,status=status.HTTP_200_OK)
                
        else:
            json ={
                "massage":"There is no Stars",
            }
            return  Response(json,status=status.HTTP_400_BAD_REQUEST)
        



class RateViewset(viewsets.ModelViewSet):
    queryset = RateModel.objects.all()
    serializer_class = RateSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    
    # to override on update and create functions to viewsets
    def update(self, request, *args, **kwargs):
        response = {
            'message':'This is not the way to update or create rating'
        }
        return Response (response,status=status.HTTP_400_BAD_REQUEST)
    def create(self, request, *args, **kwargs):
        response = {
            'message':'This is not the way to update or create rating'
        }
        return Response (response,status=status.HTTP_400_BAD_REQUEST)

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    
    def create(self,request,*args,**kwargs):
        serializer =  self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        token,created = Token.objects.get_or_create(user=serializer.instance)
        return Response(
            {'token':token.key},status=status.HTTP_201_CREATED
        )
    def list(self,request,*args,**kwargs):
        response = {'message':"You cann't create list to users"}
        Response(response,status=status.HTTP_400_BAD_REQUEST)
        
    def update(self,request,*args,**kwargs):
        response = {'message':"You cann't update user"}
        Response(response,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,*args,**kwargs):
        response = {'message':"You cann't delete user"}
        Response(response,status=status.HTTP_400_BAD_REQUEST)