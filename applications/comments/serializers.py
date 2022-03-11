from rest_framework import serializers

from applications.comments.models import Comments


class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user_id'] = request.user.id
        comments = Comments.objects.create(**validated_data)
        return comments

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['user'] = f'{instance.user}'
        return rep
