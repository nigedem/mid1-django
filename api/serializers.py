from rest_framework import serializers
from api.models import StudentData

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentData
        fields = "__all__"