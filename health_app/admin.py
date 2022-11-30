from django.contrib import admin
from .models import User, Comorbidity, Meal, DailyValue, Unit, Recipe

# Register your models here.
admin.site.register(User)
admin.site.register(Comorbidity)
admin.site.register(Meal)
admin.site.register(DailyValue)
admin.site.register(Unit)
admin.site.register(Recipe)