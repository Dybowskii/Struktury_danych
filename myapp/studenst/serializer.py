from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    add = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = Student
        fields = ('pk', 'first_name', 'last_name', 'email', 'classroom','owner','price','add')