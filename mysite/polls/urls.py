from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeDetailView.as_view(), name='trangchu'),
]