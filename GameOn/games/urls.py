from django.urls import path
from . import views

urlpatterns = [
    path('', views.GamesList.as_view()),
    path('<int:pk>/', views.GamesDetail.as_view()),
]