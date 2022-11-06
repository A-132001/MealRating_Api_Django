from unittest.util import _MAX_LENGTH
from wsgiref import validate
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator
import uuid
class MealModel(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    def __str__(self):
        return self.title

class RateModel(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    meal = models.ForeignKey(MealModel,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    class Meta:
        unique_together = (('user','meal'),)
        index_together = (('user','meal'),)
        
