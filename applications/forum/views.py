from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from .models import Question, Answer
from .permissions import IsQuestionAuthor
from .serializers import QuestionSerializer, AnswerSerializers


class QuestionListView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    pagination_class = PageNumberPagination


class QuestionCreateView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, ]

    def get_serializer_context(self):
        return {'request': self.request}


class QuestionUpdateView(generics.UpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsQuestionAuthor, ]


class QuestionDeleteView(generics.DestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsQuestionAuthor, ]


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializers
    permission_classes = [IsAuthenticated, IsQuestionAuthor, ]

