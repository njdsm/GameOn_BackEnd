from django.urls import path
from . import views

urlpatterns = [
    path('', views.CurrentGamesList.as_view()),
    path('<int:pk>/', views.CurrentGamesDetail.as_view()),
]