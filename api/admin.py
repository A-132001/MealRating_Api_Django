from django.contrib import admin
from .models import MealModel,RateModel


class RateingAdmin(admin.ModelAdmin):
    list_display = ['id',"meal",'user','stars']
    list_filter =['meal','user']

class MealAdmin(admin.ModelAdmin):
    list_display = ['id','title','description']
    search_fields = ['title','description']
    list_filter = ['title','description']
    
admin.site.register(MealModel,MealAdmin)
admin.site.register(RateModel,RateingAdmin)


