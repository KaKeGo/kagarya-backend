from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework import permissions, status

from .models import (
    About,
)
from .serializers import (
    AboutListSerializer,
    AboutCreateSerializer,
    AboutUpdateSerializer,
)

# Create your views here.


@method_decorator(csrf_protect, name='dispatch')
class AboutListView(generics.ListAPIView, mixins.ListModelMixin):
    queryset = About.objects.all()
    serializer_class = AboutListSerializer
    permission_classes = (permissions.AllowAny, )
    
@method_decorator(csrf_protect, name='dispatch')
class AboutUpdateView(APIView):
    permission_classes = (permissions.AllowAny, )
    
    def get(self, request, slug):
        about = About.objects.filter(slug=slug)
        about = AboutUpdateSerializer(about, many=True)
        return Response(about.data, status=status.HTTP_200_OK)
    
    def put(self, request, slug):
        about = get_object_or_404(About, slug=slug)
        serializer = AboutUpdateSerializer(about, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Updated successfully'}, status=status.HTTP_201_CREATED)
        return Response({'error': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)
