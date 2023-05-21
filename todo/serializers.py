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
        
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.completed = validated_data.get('completed', instance.completed)
        instance.save()
