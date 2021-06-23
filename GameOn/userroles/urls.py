from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserRolesList.as_view()),
    path('<int:pk>/', views.UserRolesDetail.as_view()),
]