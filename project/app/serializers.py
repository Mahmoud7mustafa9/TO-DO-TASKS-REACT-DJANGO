from rest_framework import serializers
from .models import Project

class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields =("title","start_date" ,"end_date","created","comments","status","id")
        read_only_fields = ['id'] 
