# TODO: опишите сериализаторы
from rest_framework import serializers
from measurements.models import Project, Measurement


class ProjectSerializer(serializers.ModelSerializer):

    # подключаем модель
    class Meta:
        model = Project
        #все поля выводим
        fields = ('id', 'name', 'latitude', 'longitude', 'created_at', 'updated_at')

class MeasurementSerializer(serializers.ModelSerializer):
    # подключаем модель
    class Meta:
        model = Measurement
        # все поля выводим
        fields = ('id', 'value', 'project', 'created_at', 'updated_at')



