from django.urls import path
from . import views

urlpatterns = [
    path('', views.getStudentData),
    path('post/', views.setStudentData)
]