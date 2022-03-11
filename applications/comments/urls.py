from django.urls import path

from applications.comments.views import CommentsListView, CommentsCreateView, CommentsUpdateView, CommentsDeleteView

urlpatterns = [
    path('comm-list/', CommentsListView.as_view()),
    path('comm-create/', CommentsCreateView.as_view()),
    path('comm-update/<int:pk>/', CommentsUpdateView.as_view()),
    path('comm-delete/<int:pk>/', CommentsDeleteView.as_view())
]