from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import QuestionListView, QuestionCreateView, QuestionUpdateView, QuestionDeleteView, AnswerViewSet

router = DefaultRouter()
router.register('answer', AnswerViewSet)

urlpatterns = [
    path('qes-list/', QuestionListView.as_view()),
    path('qes-create/', QuestionCreateView.as_view()),
    path('qes-update/<int:pk>/', QuestionUpdateView.as_view()),
    path('qes-delete/<int:pk>/', QuestionDeleteView.as_view()),
    path('', include(router.urls)),


]
