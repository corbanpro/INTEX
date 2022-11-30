from django.db import models
from datetime import datetime

class Comorbidity(models.Model) :
    kidneyDiseaseStage = models.IntegerField()
    highBloodPressure = models.BooleanField()
    diabetes = models.BooleanField()

    class Meta:
        db_table = 'Comorbidities'

class User(models.Model) :
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    sex = models.CharField(max_length=1)
    height = models.IntegerField()
    weight = models.IntegerField()
    birthDate = models.DateField(default= datetime.now, blank= True, max_length=5)
    comorbidity = models.ForeignKey(Comorbidity, default= 1, blank= False, on_delete=models.DO_NOTHING)

    def __str__(self):
        fullName = self.lastName + ", " + self.firstName
        return (fullName)

    class Meta:
        db_table = 'users'


class Recipe(models.Model) :
    name = models.CharField(max_length=50)
    calories = models.FloatField(default= 0)
    fat = models.FloatField(default= 0)
    protein = models.FloatField(default= 0)
    carbs = models.FloatField(default= 0)
    potassium = models.FloatField(default= 0)
    phosphorous = models.FloatField(default= 0)
    sodium = models.FloatField(default= 0)
    water = models.FloatField(default= 0)
    
    def __str__(self):
        return (self.name)
    
    class Meta:
        db_table = 'Recipes'

class Meal(models.Model) :
    datetime = models.DateTimeField(default= datetime.now, blank= True, max_length=5)
    recipe = models.ForeignKey(Recipe, default= 1, blank= False, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, default= 1, blank= False, on_delete=models.DO_NOTHING)


    def __str__(self):
        
        return (Recipe.name + ', ' + self.datetime)
    
    class Meta:
        db_table = 'Meals'


class DailyValue(models.Model) :
    calories = models.FloatField()
    fat = models.FloatField()
    protein = models.FloatField()
    carbs = models.FloatField()
    potassium = models.FloatField()
    phosphorus = models.FloatField()
    sodium = models.FloatField()
    comorbidity = models.OneToOneField(Comorbidity, default= 1, on_delete=models.CASCADE)
  

    class Meta:
        db_table = 'Daily Values'
        

class Unit(models.Model) :
    nutrient = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)


    def __str__(self):
        name = self.nutrient + '(' + self.unit + ')' 
        return (name)   

    class Meta:
        db_table = 'Units'