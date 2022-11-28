from django.contrib import admin
from .models import user, comorbidity, meal, dailyValue, unit, recipe

# Register your models here.
admin.site.register(user)
admin.site.register(comorbidity)
admin.site.register(meal)
admin.site.register(dailyValue)
admin.site.register(unit)
admin.site.register(recipe)