from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeDetailView.as_view(), name='trangchu'),
    path('questions/', views.questions, name='questions'),
    path('choice/<int:question_id>/', views.addChoice, name='new_choice'),
]