import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import WeatherSerializer
import datetime


class WeatherAPIView(APIView):
    def get(self, request, pk):
        units = 'metric'
        apikey = ''
        url = f'http://api.openweathermap.org/data/2.5/weather?{pk}&units={units}&apikey={apikey}'
        response = requests.get(url)
        if response.status_code == 200:
            item = response.json()
            item['timestamp'] = datetime.datetime.now()
            result = WeatherSerializer(item).data
        elif response.status_code == 404:
            result = {"detail": "not found"}
        return Response(result)
