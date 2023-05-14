from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
from django.contrib import auth

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status

from .models import (
    CustomUser,
    UserProfile,
)
from .serializers import (
    ProfilesListSerializer,
)

# Create your views here.


class CheckAuthenticatedView(APIView):
    def get(self, request, format=None):
        try:
            isAuthenticated = CustomUser.is_authenticated
            
            if isAuthenticated:
                return Response({'isAuthenticated': 'success'}, status=status.HTTP_200_OK)
            else:
                return Response({'isAuthenticated': 'User not authenticated'},  status=status.HTTP_403_FORBIDDEN)
        except:
            return Response({'error': 'Something went wrong when checking authentication'})

class ProfileListView(APIView):
    permission_classes = (permissions.AllowAny, )
    
    def get(self, request, format=None):
        try:
            profiles = UserProfile.objects.all()
            
            profiles = ProfilesListSerializer(profiles, many=True)
            
            return Response(profiles.data, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Something went wrong and cant show profile list.'})
        
