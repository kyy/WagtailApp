from rest_framework import serializers
from .models import Datatable


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datatable
        fields = '__all__'
