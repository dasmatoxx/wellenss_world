from rest_framework import serializers

from .models import Question, Answer


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('id', 'category', 'title', 'image', 'problem', 'public_date')

    def create(self, validated_data):
        requests = self.context.get('request')
        validated_data['author_id'] = requests.user.id
        print(requests.user.id)
        question = Question.objects.create(**validated_data)
        return question

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['category'] = instance.category.title
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
        rep['author'] = instance.author.email
        rep['solutions'] = AnswerSerializers(Answer.objects.filter(questions=instance.id), many=True).data
        rep['category'] = instance.category.title
        return rep
