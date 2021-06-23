from django.urls import path
from . import views

urlpatterns = [
    path('', views.StatsList.as_view()),
    path('<int:pk>/', views.StatsDetail.as_view()),
]