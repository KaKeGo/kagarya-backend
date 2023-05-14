from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
from django.contrib import auth

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status, generics

from .models import (
    CustomUser,
    UserProfile,
)
from .serializers import (
    ProfilesListSerializer,
    UserCreateSerializer,
)

# Create your views here.


class CheckAuthenticatedView(APIView):
    def get(self, request):
        try:
            isAuthenticated = CustomUser.is_authenticated
            
            if isAuthenticated:
                return Response({'isAuthenticated': 'success'}, status=status.HTTP_200_OK)
            else:
                return Response({'isAuthenticated': 'User not authenticated'},  status=status.HTTP_403_FORBIDDEN)
        except:
            return Response({'error': 'Something went wrong when checking authentication'})

class CreateUserAccount(APIView): 
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Accout was created'}, status=status.HTTP_200_OK)
        return Response({'error': 'Something went wrong with creating user'}, status=status.HTTP_400_BAD_REQUEST)
        
        # try:
        #     if len(username) < 2:
        #             return Response({'error': 'Username must be longer than 2 characters.'})
        #     if password == re_password:
        #         if CustomUser.objects.filter(email=email).exists():
        #             return Response({'error': 'Account with this email already exists.'})
        #         else:
        #             if len(password) < 6:
        #                 return Response({'error': 'Password must have at least 6 characters.'})
        #             else:
        #                 user = CustomUser.objects.create(
        #                     email=email,
        #                     username=username,
        #                     password=password,
        #                 )
        #                 user.save()
        #                 return Response({'success': 'Account created successfully.'})
        #     else:
        #         return Response({'error': 'Password do not match'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        # except:
        #     return Response({'error': 'Something went wrong with creating user try again.'}, status=status.HTTP_400_BAD_REQUEST)
 
class ProfileListView(APIView):
    permission_classes = (permissions.AllowAny, )
    
    def get(self, request):
        try:
            profiles = UserProfile.objects.all()
            
            profiles = ProfilesListSerializer(profiles, many=True)
            
            return Response(profiles.data, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Something went wrong and cant show profile list.'})
        
