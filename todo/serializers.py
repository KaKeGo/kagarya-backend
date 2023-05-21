from rest_framework import serializers

from .models import (
    ToDo,
)


class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = (
            'title', 'description', 'completed', 'date_created', 'slug'
        )

class ToDoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = (
            'title', 'description'
        )
        
class ToDoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = (
            'title', 'desciption', 'completed'
        )
