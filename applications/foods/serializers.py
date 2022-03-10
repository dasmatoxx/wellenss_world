from rest_framework import serializers

from .models import Food, FoodImage


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
        rep['images'] = FoodImageSerializer(FoodImage.objects.filter(foods=instance.id), many=True,
                                               context=self.context).data
        rep['category'] = instance.category.title
        return rep
