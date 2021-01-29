from rest_framework import serializers
from .models import Studentfrom

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Studentfrom
        fields= '__all__'