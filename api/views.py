from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from api.models import Courses
from api.serializers import coursesModelSerializer
from rest_framework.viewsets import ModelViewSet



class coursesViewsetsview(ModelViewSet): 
    serializer_class=coursesModelSerializer
    queryset=Courses.objects.all()  