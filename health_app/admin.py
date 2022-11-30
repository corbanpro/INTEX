from django.contrib import admin
from .models import User, DvDeterminate, Meal, DailyValue, Unit, Recipe

# Register your models here.
admin.site.register(User)
admin.site.register(DvDeterminate)
admin.site.register(Meal)
admin.site.register(DailyValue)
admin.site.register(Unit)
admin.site.register(Recipe)