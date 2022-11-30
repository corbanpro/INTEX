from django.db import models
from datetime import datetime
import django


class DailyValue(models.Model) :
    description = models.CharField(null=True, max_length=50)
    calories = models.FloatField()
    fat = models.FloatField()
    protein = models.FloatField()
    carbs = models.FloatField()
    potassium = models.FloatField()
    phosphorus = models.FloatField()
    sodium = models.FloatField()
    water = models.FloatField(default= 20)

    class Meta:
        db_table = 'DailyValues'

    def __str__(self):
        return (self.description)
        

class DvDeterminate(models.Model) :
    kidneyDiseaseStage = models.IntegerField()
    highBloodPressure = models.BooleanField()
    diabetes = models.BooleanField()
    sex = models.CharField(max_length=10, default= 'M')
    daily_value = models.ForeignKey(DailyValue, default= 2, on_delete=models.DO_NOTHING)



    def __str__(self):
        return (f'sex: {self.sex}, KDS: {self.kidneyDiseaseStage}, HBP: {self.highBloodPressure}, DB: {self.diabetes}')
    class Meta:
        db_table = 'DailyValueDeterminates'

class User(models.Model) :
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    height = models.IntegerField()
    weight = models.IntegerField()
    birthDate = models.DateField(default= datetime.now, blank= True, max_length=5)
    dv_determinate = models.ForeignKey(DvDeterminate, default= 1, blank= False, on_delete=models.DO_NOTHING)

    def __str__(self):
        fullName = self.lastName + ", " + self.firstName
        return (fullName)

    class Meta:
        db_table = 'Users'


class Recipe(models.Model) :
    name = models.CharField(max_length=50)
    calories = models.FloatField(default= 0)
    fat = models.FloatField(default= 0)
    protein = models.FloatField(default= 0)
    carbs = models.FloatField(default= 0)
    potassium = models.FloatField(default= 0)
    phosphorus = models.FloatField(default= 0)
    sodium = models.FloatField(default= 0)
    water = models.FloatField(default= 0)
    
    def __str__(self):
        return (self.name)
    
    class Meta:
        db_table = 'Recipes'

class Meal(models.Model) :
    date = models.DateField(default= django.utils.timezone.now, blank= True, max_length=5)
    recipe = models.ForeignKey(Recipe, default= 1, blank= False, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, default= 1, blank= False, on_delete=models.DO_NOTHING)


    def __str__(self):
        return (str(self.id))
    
    class Meta:
        db_table = 'Meals'



class Unit(models.Model) :
    nutrient = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)


    def __str__(self):
        name = self.nutrient + '(' + self.unit + ')' 
        return (name)   

    class Meta:
        db_table = 'Units'