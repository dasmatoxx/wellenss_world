from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from applications.foods.models import Food

User = get_user_model()


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                             related_name='comment')
    food = models.ForeignKey(Food, on_delete=models.CASCADE,
                             related_name='comment')
    comment = models.TextField()
    rating = models.IntegerField(default=1, validators=[MaxValueValidator(10),
                                                        MinValueValidator(1)])

    def __str__(self):
        return self.food.title
