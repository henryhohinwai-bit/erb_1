from django.contrib import admin

# Register your models here.

from .models import Chef, Restaurant, Dish


admin.site.register(Chef)
admin.site.register(Restaurant)
admin.site.register(Dish)

