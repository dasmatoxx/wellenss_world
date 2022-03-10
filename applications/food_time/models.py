from django.db import models
from applications.food_time.utils import slug_generator


class Category(models.Model):
    title = models.CharField(max_length=50)
    time = models.CharField(max_length=20, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.title

