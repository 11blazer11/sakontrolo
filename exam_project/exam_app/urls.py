from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('film/', views.films_view, name="film"),
]
