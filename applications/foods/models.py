from django.db import models

from applications.food_time.models import Category


class Food(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='foods')

    title = models.CharField(max_length=20)
    ingredients = models.TextField()
    calories = models.PositiveIntegerField(default=1)
    description = models.TextField()

    def __str__(self):
        return self.title


class FoodImage(models.Model):
    foods = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='image')

    image = models.ImageField(upload_to='product_photo')

    def __str__(self):
        return self.foods.title



