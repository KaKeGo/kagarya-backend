from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status

from users.models import User

from .models import (
    TodoPlan,
    Todo,
    Task,
)
from .serializers import (
    
    TodoPlanListSerializer,
    TodoPlanCreateSerializer,
    
    TodoSerializer,
    TodoCreateSerializer,
    
    TaskSerializer,
    TaskCreateSerializer,
)

# Create your views here.


#----> Todo Plan
@method_decorator(csrf_protect, name='dispatch')
class TodoPlanView(APIView):
    permission_classes = (permissions.AllowAny, )
    
    def get(self, request):
        plan = TodoPlan.objects.all()
        plan = TodoPlanListSerializer(plan, many=True, context={'request': request})
        return Response(plan.data, status=status.HTTP_200_OK)

@method_decorator(csrf_protect, name='dispatch')
class TodoDetailPlanView(APIView):
    permission_classes = (permissions.AllowAny, )
    
    def get(self, request, slug):
        plan = TodoPlan.objects.filter(slug=slug)
        plan = TodoPlanListSerializer(plan, many=True)
        return Response(plan.data, status=status.HTTP_200_OK)

@method_decorator(csrf_protect, name='dispatch')
class TodoPlanCreateView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        serializer = TodoPlanCreateSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(
                    author = self.request.user
                )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#----> Todo
@method_decorator(csrf_protect, name='dispatch')
class TodoView(APIView):
    permission_classes = (permissions.AllowAny, )
    
    def get(self, request, slug, title):
        plan = TodoPlan.objects.filter(slug=slug, title=title)
        plan = TodoPlanListSerializer(plan, many=True)
        
        todo = Todo.objects.all()
        todo = TodoSerializer(todo, many=True)
        context = [todo.data, plan.data]
        return Response(context, status=status.HTTP_200_OK)
    

@method_decorator(csrf_protect, name='dispatch')
class TodoDetailView(APIView):
    permission_classes = (permissions.AllowAny, )
    
    def get(self, request, slug):
        todo = Todo.objects.filter(slug=slug)
        todo = TodoSerializer(todo, many=True, context={'request': request})
        return Response(todo.data, status=status.HTTP_200_OK)
 
# @method_decorator(csrf_protect, name='dispatch')
class TodoCreateView(APIView):
    permission_classes = (permissions.AllowAny, )
    
    def post(self, request):
        serializer = TodoCreateSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
#----> Task
class TaskDetailView(APIView):
    permission_classes = (permissions.AllowAny, )
    
    def get(self, request, name):
        task = Task.objects.filter(name=name)
        task = TaskSerializer(task, many=True)
        return Response(task.data, status=status.HTTP_200_OK)

class TaskCreateView(APIView):
    permission_classes = (permissions.AllowAny, )
    
    def post(self, request):
        serializer = TaskCreateSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  
  
  
# @method_decorator(csrf_protect, name='dispatch')
# class ToDoDetailView(APIView):
#     permission_classes = (permissions.AllowAny, )
    
#     def get(self, request, slug):
#         todo = ToDo.objects.filter(slug=slug)
        
#         todo = ToDoListSerializer(todo, many=True)
        
#         return Response(todo.data, status=status.HTTP_200_OK)
        

# @method_decorator(csrf_protect, name='dispatch')
# class ToDoUpdateView(APIView):
#     permission_classes = (permissions.IsAdminUser, )
    
#     def get(self, request, slug):
#         todo = ToDo.objects.filter(slug=slug)
  
#         todo = ToDoUpdateSerializer(todo, many=True)
        
#         return Response(todo.data, status=status.HTTP_200_OK)
    
#     def put(self, request, slug):
#         todo = get_object_or_404(ToDo, slug=slug)
#         serializer = ToDoUpdateSerializer(todo, data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'success': 'Todo was updated successfully'}, status=status.HTTP_200_OK)
#         return Response({'error': 'Someting went wrong with updating todo.'}, status=status.HTTP_400_BAD_REQUEST)

# @method_decorator(csrf_protect, name='dispatch')
# class ToDoDeleteView(APIView):
#     permission_classes = (permissions.IsAdminUser, )
    
#     def get(self, request, slug):
#         todo = ToDo.objects.filter(slug=slug)
        
#         todo = ToDoUpdateSerializer(todo, many=True)
        
#         return Response(todo.data, status=status.HTTP_200_OK)
    
#     def delete(self, request, slug):
#         todo = ToDo.objects.get(slug=slug)
        
#         todo.delete()
        
#         return Response(status=status.HTTP_204_NO_CONTENT)
    