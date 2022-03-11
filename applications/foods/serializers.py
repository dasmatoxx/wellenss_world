from rest_framework import serializers

from .models import Food, FoodImage
from ..comments.models import Comments
from ..comments.serializers import CommentsSerializer


class FoodImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodImage
        fields = ('image', )

    def _get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            request = self.context.get('request')
            if request is not None:
                url = request.build_absolute_uri(url)
        else:
            url = ''
        return url

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['image'] = self._get_image_url(instance)
        return rep


class FoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = ('title', 'ingredients', 'calories', 'description', 'category', )

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        total_rating = [i.rating for i in instance.comment.all()]
        if len(total_rating) != 0:
            rep['total_rating'] = sum(total_rating) / len(total_rating)
        else:
            rep['total_rating'] = 0
        rep['images'] = FoodImageSerializer(FoodImage.objects.filter(foods=instance.id), many=True,
                                            context=self.context).data
        rep['category'] = instance.category.title
        rep['comment'] = CommentsSerializer(Comments.objects.filter(food=instance.id),
                                            many=True).data
        return rep


