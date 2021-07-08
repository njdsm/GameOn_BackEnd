from django.urls import path
from . import views

urlpatterns = [
    path('', views.OwnersList.as_view()),
    path('<str:key>/', views.OwnersDetail.as_view()),
]
