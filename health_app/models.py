from django.db import models
from datetime import datetime

class comorbidity(models.Model) :
    KidneyDiseaseStage = models.IntegerField()
    highBloodPressure = models.BooleanField()
    stroke = models.BooleanField()
    obesity = models.BooleanField()
    diabetes = models.BooleanField()
    heartDisease = models.BooleanField()
    smoker = models.BooleanField()

    class Meta:
        db_table = 'Comorbidities'

class user(models.Model) :
    email = models.EmailField( max_length=254)
    password = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    sex = models.CharField(max_length=1)
    height = models.IntegerField()
    weight = models.IntegerField()
    birthDate = models.DateField(default= datetime.now, blank= True, max_length=5)
    comorbidity = models.ForeignKey(comorbidity, default= 1, blank= False, on_delete=models.DO_NOTHING)

    def __str__(self):
        fullName = self.lastName + ", " + self.firstName
        return (fullName)

    class Meta:
        db_table = 'users'


class recipe(models.Model) :
    name = models.CharField(max_length=50)
    calories = models.FloatField()
    fat = models.FloatField()
    protein = models.FloatField()
    carbs = models.FloatField()
    water = models.FloatField()
    potassium = models.FloatField()
    phosphorous = models.FloatField()
    sodium = models.FloatField()
    
    def __str__(self):
        return (self.name)
    
    class Meta:
        db_table = 'Recipes'

class meal(models.Model) :
    datetime = models.DateTimeField(default= datetime.now, blank= True, max_length=5)
    recipe = models.ForeignKey(recipe, default= 1, blank= False, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(user, default= 1, blank= False, on_delete=models.DO_NOTHING)


    def __str__(self):
        
        return (recipe.name + ', ' + self.datetime)
    
    class Meta:
        db_table = 'Meals'


class dailyValue(models.Model) :
    calories = models.FloatField()
    fat = models.FloatField()
    protein = models.FloatField()
    carbs = models.FloatField()
    water = models.FloatField()
    potassium = models.FloatField()
    phosphorous = models.FloatField()
    sodium = models.FloatField()
    comorbidity = models.OneToOneField(comorbidity, default= 1, on_delete=models.CASCADE)
  

    class Meta:
        db_table = 'Daily Values'
        

class unit(models.Model) :
    nutrient = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)


    def __str__(self):
        name = self.nutrient + '(' + self.unit + ')' 
        return (name)   

    class Meta:
        db_table = 'Units'