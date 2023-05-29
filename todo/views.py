from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status

from .models import (
    ToDo,
)
from .serializers import (
    ToDoListSerializer,
    ToDoCreateSerializer,
    ToDoUpdateSerializer,
)

# Create your views here.


@method_decorator(csrf_protect, name='dispatch')
class ToDoListView(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request):
        todo = ToDo.objects.all()
        
        todo = ToDoListSerializer(todo, many=True)
        
        return Response(todo.data, status=status.HTTP_200_OK)

@method_decorator(csrf_protect, name='dispatch')
class ToDoCreateView(APIView):
    permission_classes = (permissions.IsAdminUser, )
    
    def post(self, request):
        serializer = ToDoCreateSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Todo was created successfuly'}, status=status.HTTP_201_CREATED)
        return Response({'error': 'Somethin went wrong with creating todo.'}, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_protect, name='dispatch')
class ToDoDetailView(APIView):
    permission_classes = (permissions.AllowAny, )
    
    def get(self, request, slug):
        todo = ToDo.objects.filter(slug=slug)
        
        todo = ToDoListSerializer(todo, many=True)
        
        return Response(todo.data, status=status.HTTP_200_OK)
        

@method_decorator(csrf_protect, name='dispatch')
class ToDoUpdateView(APIView):
    permission_classes = (permissions.IsAdminUser, )
    
    def get(self, request, slug):
        todo = ToDo.objects.filter(slug=slug)
  
        todo = ToDoUpdateSerializer(todo, many=True)
        
        return Response(todo.data, status=status.HTTP_200_OK)
    
    def put(self, request, slug):
        todo = get_object_or_404(ToDo, slug=slug)
        serializer = ToDoUpdateSerializer(todo, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Todo was updated successfully'}, status=status.HTTP_200_OK)
        return Response({'error': 'Someting went wrong with updating todo.'}, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_protect, name='dispatch')
class ToDoDeleteView(APIView):
    permission_classes = (permissions.IsAdminUser, )
    
    def get(self, request, slug):
        todo = ToDo.objects.filter(slug=slug)
        
        todo = ToDoUpdateSerializer(todo, many=True)
        
        return Response(todo.data, status=status.HTTP_200_OK)
    
    def delete(self, request, slug):
        todo = ToDo.objects.get(slug=slug)
        
        todo.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
    