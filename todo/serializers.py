from rest_framework import serializers

from .models import (
    TodoPlan,
    Todo,
    Task,
)
 
#----> Task
class TaskSerializer(serializers.ModelSerializer):
    '''
    To List task's
    '''
    class Meta:
        model = Task
        fields = ['name', 'complited']

class TaskCreateSerializer(serializers.ModelSerializer):
    '''
    To Create task list
    '''
    class Meta:
        model = Task
        fields = ['name',]
        
    def create(self, validated_data):
        tasks = Task.objects.create(**validated_data)
        return tasks

#----> Todo
class TodoSerializer(serializers.ModelSerializer):
    '''
    To List Todo list
    '''
    tasks = TaskSerializer(many=True, required=False)
    
    class Meta:
        model = Todo
        fields = ['title', 'description', 'category', 'tasks', 'completed', 'date_created', 'slug']

class TodoTaskCreateSerializer(serializers.ModelSerializer):
    '''
    To Create and add Task in Todo model | Not working yet
    '''
    task = TaskCreateSerializer(many=True, read_only=False)
    
    class Meta:
        model = Todo
        fields = ['task',]
        
    def update(self, instance, validated_data):
        tasks_data = validated_data.pop('task')
        instance = super(TodoTaskCreateSerializer, self).update(instance, validated_data)
        
        for task_data in tasks_data:
             task_qs = Task.objects.filter(name__iexact=task_data['name'])
             
             if task_qs.exists():
                 task = task_qs.first()
             else:
                 task = Task.objects.create(**task_data)
                 
        instance.task.add(task)
        return instance

class TodoCreateSerializer(serializers.ModelSerializer):
    '''
    To Create Todo
    '''
    class Meta:
        model = Todo
        fields = ['title', 'description', 'category']
        
    def create(self, validated_data):
        todo = Todo.objects.create(**validated_data)
        return todo

class TodoUpdateSerializer(serializers.ModelSerializer):
    '''
    To Update Todo
    '''
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
    '''
    To Plan list
    '''
    todo = TodoSerializer(many=True, required=False)
    
    class Meta:
        model = TodoPlan
        fields = ['name', 'todo', 'author_name',]

class TodoPlanCreateTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoPlan
        fields = ['name', 'todo',]   
    
    def create(self, validate_data):
        instance = Todo.objects.create(**validate_data)
        return instance
        

class TodoPlanCreateSerializer(serializers.ModelSerializer):
    '''
    To Plan create
    '''
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
