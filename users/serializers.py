from rest_framework import serializers

from .models import (
    CustomUser,
    UserProfile,
)


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'username',) 

class ProfilesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
                    'p_username', 
                    #Function
                    'get_email', 'get_online_status'
                  )
