from  .views import MealViewset,RateViewset
from django.urls import path,include
from rest_framework import routers

app_name ='api'
router = routers.DefaultRouter()
router.register('meals',MealViewset)
router.register('rating',RateViewset)

urlpatterns = [
    path("",include(router.urls))
]