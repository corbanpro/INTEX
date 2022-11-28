from django.contrib import admin
from .models import patient, ingredient, meal, dailyValue, units

# Register your models here.
admin.site.register(patient)
admin.site.register(ingredient)
admin.site.register(meal)
admin.site.register(dailyValue)
admin.site.register(units)