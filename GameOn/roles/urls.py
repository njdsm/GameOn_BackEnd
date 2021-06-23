from django.urls import path
from . import views

urlpatterns = [
    path('', views.RolesList.as_view()),
    path('<int:pk>/', views.RolesDetail.as_view()),
]