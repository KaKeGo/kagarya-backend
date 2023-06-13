from rest_framework import serializers

from .models import (
    TodoPlan,
    Todo,
    Task,
)
 
#----> Task
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['name', 'complited']

class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['name',]
        
    def create(self, validated_data):
        tasks = Task.objects.create(**validated_data)
        return tasks

#----> Todo
class TodoSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, required=False)
    
    class Meta:
        model = Todo
        fields = ['title', 'description', 'category', 'tasks', 'completed', 'date_created', 'slug']

class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'category']
        
    def create(self, validated_data):
        todo = Todo.objects.create(**validated_data)
        return todo

class TodoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'category', 'completed']

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.category = validated_data.get('category', instance.category)
        instance.completed = validated_data.get('completed', instance.completed)
        instance.save()
        return instance

#---> Todo Plan
class TodoPlanListSerializer(serializers.ModelSerializer):
    todo = TodoSerializer(many=True, required=False)
    
    class Meta:
        model = TodoPlan
        fields = ['name', 'todo', 'author_name',]

class TodoPlanCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoPlan
        fields = ['name']
    
    def validate_title(self, title):
        if len(title) < 4:
            raise ValueError('Title must be longer')
        return title
    
    def create(self, validated_data):
        plan = TodoPlan.objects.create(**validated_data)
        return plan
