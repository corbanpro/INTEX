from django.db import models
from datetime import datetime

class patient(models.Model) :
    email = models.EmailField( max_length=254)
    password = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    sex = models.CharField(max_length=1)
    height = models.IntegerField()
    weight = models.IntegerField()
    highBloodPressure = models.BooleanField()
    stroke = models.BooleanField()
    heartDisease = models.BooleanField()
    diabetes = models.BooleanField()
    KidneyDiseaseStage = models.IntegerField()

    def __str__(self):
        fullName = self.lastName + ", " + self.firstName
        return (fullName)

    class Meta:
        db_table = 'patients'


class meal(models.Model) :
    name = models.CharField(max_length=50)
    datetime = models.DateTimeField(default= datetime.now, blank= True, max_length=5)
    calories = models.IntegerField()
    fat = models.IntegerField()
    protein = models.IntegerField()
    carbs = models.IntegerField()
    potassium = models.IntegerField()
    phosphorous = models.IntegerField()
    sodium = models.IntegerField()
    water = models.IntegerField()
    patient = models.ForeignKey(patient, default= 1, blank= False, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return (self.name)
    
    class Meta:
        db_table = 'meals'


class ingredient(models.Model) :
    name = models.CharField(max_length=25)
    calories = models.IntegerField()
    fat = models.IntegerField()
    protein = models.IntegerField()
    carbs = models.IntegerField()
    potassium = models.IntegerField()
    phosphorous = models.IntegerField()
    sodium = models.IntegerField()
    meal = models.ManyToManyField(meal, blank= True)

    def __str__(self):
        return (self.name)   

    class Meta:
        db_table = 'ingredients'


class dailyValue(models.Model) :
    Comorbidity = models.CharField(max_length=25)
    calories = models.IntegerField()
    fat = models.IntegerField()
    protein = models.IntegerField()
    carbs = models.IntegerField()
    potassium = models.IntegerField()
    phosphorous = models.IntegerField()
    sodium = models.IntegerField()
    water = models.IntegerField()


    def __str__(self):
        return (self.Comorbidity)   

    class Meta:
        db_table = 'dailyValues'
        

class units(models.Model) :
    nutrient = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)


    def __str__(self):
        name = self.nutrient + '(' + self.unit + ')' 
        return (name)   

    class Meta:
        db_table = 'units'