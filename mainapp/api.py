import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import WeatherSerializer
import datetime


class WeatherAPIView(APIView):
    def get(self, request, pk):
        units = 'metric'
        apikey = 'd3fb8a3c27a99a41a336eb043a341986'
        url = f'http://api.openweathermap.org/data/2.5/weather?{pk}&units={units}&apikey={apikey}'
        item = requests.get(url).json()
        item['timestamp'] = datetime.datetime.now()
        result = WeatherSerializer(item).data
        return Response(result)
