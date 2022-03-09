from django.contrib import admin

# Register your models here.
from applications.food_time.models import Category

admin.site.register(Category)
