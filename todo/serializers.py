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
        
    def validate_title(self, title):
        if len(title) < 0:
            raise ValueError('Title must be less than zero.')
        return title
    
    def validate_description(self, description):
        if len(description) < 0:
            raise ValueError('Description must be less than zero.')
        return description
        
    def create(self, validated_data):
        todo = ToDo.objects.create(**validated_data)
        return todo
        
class ToDoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = (
            'title', 'description', 'completed'
        )
        
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.completed = validated_data.get('completed', instance.completed)
        instance.save()
