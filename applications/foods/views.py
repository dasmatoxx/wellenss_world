from rest_framework.generics import ListAPIView

from .models import Food
from .serializers import FoodSerializer


class FoodListView(ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

