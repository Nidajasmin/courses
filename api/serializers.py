from rest_framework import serializers
from api.models import Courses


class coursesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Courses
        fields="__all__"
        # fields=['name','price','description']