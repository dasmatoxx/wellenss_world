from django.contrib.auth import get_user_model
from django.db import models

from applications.food_time.models import Category

User = get_user_model()


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='question')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='question')

    title = models.TextField()
    images = models.ImageField(upload_to='', blank=True, null=True)
    problem = models.TextField()
    public_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answer')

    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer')

    solution = models.TextField()
    image = models.ImageField(upload_to='', blank=True, null=True)
    public_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question.title


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='like')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE,
                               related_name='like')
    like = models.BooleanField(default=False)

    def __str__(self):
        return self.like
