from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

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
    permission_classes = (permissions.AllowAny, )
    
    def post(self, request):
        serializer = ToDoCreateSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Todo was created successfuly'}, status=status.HTTP_201_CREATED)
        return Response({'error': 'Somethin went wrong with creating todo.'}, status=status.HTTP_400_BAD_REQUEST)
