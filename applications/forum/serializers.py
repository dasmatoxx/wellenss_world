from rest_framework import serializers

from .models import Question, Answer, Like


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('id', 'category', 'title', 'image', 'problem', 'public_date')

    def create(self, validated_data):
        requests = self.context.get('request')
        validated_data['author_id'] = requests.user.id
        question = Question.objects.create(**validated_data)
        return question

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['category'] = instance.category.title
        rep['author'] = instance.author.email
        rep['solutions'] = AnswerSerializers(Answer.objects.filter(question=instance.id),
                                            many=True).data

        total_rating = [i.rating for i in instance.review.all()]
        if len(total_rating) != 0:
            rep['total_rating'] = sum(total_rating) / len(total_rating)
        else:
            rep['total_rating'] = 0
        return rep


class AnswerSerializers(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('id', 'question', 'solution', 'image')

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author_id'] = request.user.id
        answer = Answer.objects.create(**validated_data)
        return answer

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['question'] = instance.question.title
        rep['like'] = instance.like.filter(like=True).count()
        return rep

