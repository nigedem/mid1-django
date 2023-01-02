from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from api.models import StudentData
from api.serializers import StudentSerializer

@api_view(["GET"])
def getStudentData(request):
    data = StudentData.objects.all()
    serializer = StudentSerializer(data, many=True)
    return Response(serializer.data)
     
@api_view(["POST"])
def setStudentData(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)