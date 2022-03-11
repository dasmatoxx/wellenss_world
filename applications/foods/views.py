from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework

from .models import Food
from .serializers import FoodSerializer


class FoodFilter(rest_framework.FilterSet):
    class Meta:
        model = Food
        fields = [
            'category',
        ]


class FoodListView(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_class = FoodFilter
    search_fields = ['title', ]

    def get_serializer_context(self):
        return {'request': self.request}






