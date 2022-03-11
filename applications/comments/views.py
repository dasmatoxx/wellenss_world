from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from applications.comments.models import Comments
from applications.comments.serializers import CommentsSerializer


class CommentsListView(generics.ListAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    pagination_class = PageNumberPagination


class CommentsCreateView(generics.CreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticated, ]

    def get_serializer_context(self):
        return {'request': self.request}


class CommentsUpdateView(generics.UpdateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticated, ]


class CommentsDeleteView(generics.DestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticated, ]


