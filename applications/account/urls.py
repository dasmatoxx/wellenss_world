from django.urls import path

from . import views
from applications.account.views import RegisterView, LoginView, LogoutView

urlpatterns = [
    path('reg/', RegisterView.as_view()),
    path('activate/<str:activation_code>/', views.ActivationView.as_view()),
    path('log/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
]