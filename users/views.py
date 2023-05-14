from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status

from .models import (
    CustomUser,
    UserProfile,
)
from .serializers import (
    ProfilesListSerializer,
    UserCreateSerializer,
    PasswordChangeSerializer,
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

class LoginView(APIView):
    def post(self, request):
        if 'email' not in request.data or 'password' not in request.data or 'username' not in request.data:
            return Response({'error': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return Response({'success': 'User logged in'}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credetnials'}, status=status.HTTP_401_UNAUTHORIZED)
    
class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'success': 'Successfully Logged out'}, status=status.HTTP_401_UNAUTHORIZED)
            
class ChangePasswordView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    
    def post(self, request):
         serializer = PasswordChangeSerializer(
             context={'request': request}, data=request.data
         )
         serializer.is_valid(raise_exception=True)
         request.user.set_password(serializer.validated_data['new_password'])
         request.user.save()
         return Response({'success': 'Password changed successfully'}, status=status.HTTP_204_NO_CONTENT)

class ProfileListView(APIView):
    permission_classes = (permissions.AllowAny, )
    
    def get(self, request):
        try:
            profiles = UserProfile.objects.all()
            
            profiles = ProfilesListSerializer(profiles, many=True)
            
            return Response(profiles.data, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Something went wrong and cant show profile list.'})
        
