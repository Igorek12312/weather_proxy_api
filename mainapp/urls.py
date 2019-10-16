from django.urls import path
from mainapp.api import WeatherAPIView

urlpatterns = [
    path('weather/current/<str:pk>/', WeatherAPIView.as_view()),
]