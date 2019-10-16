from rest_framework import serializers


class TemperatureSerializer(serializers.Serializer):
    C = serializers.FloatField(source='temp')


class HumiditySerializer(serializers.Serializer):
    percent = serializers.IntegerField(source='humidity')


class PressureSerializer(serializers.Serializer):
    atm = serializers.IntegerField(source='pressure')


class WeatherSerializer(serializers.Serializer):
    location = serializers.DictField(source='coord')
    title = serializers.CharField(source='name')
    timestamp = serializers.DateTimeField()

    temperature = TemperatureSerializer(source='main')
    humidity = HumiditySerializer(source='main')
    pressure = PressureSerializer(source='main')
