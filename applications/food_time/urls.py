from django.urls import path

from applications.food_time.views import CategoryListView

urlpatterns = [
    path('', CategoryListView.as_view()),
]
