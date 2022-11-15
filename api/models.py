from unittest.util import _MAX_LENGTH
from wsgiref import validate
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

class MealModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    def __str__(self):
        return self.title
    def num_of_rating_on_meal(self):
        num_rating = RateModel.objects.filter(meal=self)
        return len(num_rating)
    # avg = sumOfStar/num_rating 
    def avg_of_stars(self):
        sum = 0
        num_rating = RateModel.objects.filter(meal=self)
        for star in num_rating:
            sum += star.stars
        if sum  > 0 :
            return sum/len(num_rating)
        else:
            return 0
        
        

class RateModel(models.Model):
    id = models.AutoField(primary_key=True)
    meal = models.ForeignKey(MealModel,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    class Meta:
        unique_together = (('user','meal'),)
        index_together = (('user','meal'),)
        
