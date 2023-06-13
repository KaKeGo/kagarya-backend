from rest_framework import serializers

from .models import (
    User,
    UserProfile,
)


class UserCreateSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def validate_username(self, username):
        if len(username) < 2 or len(username) > 30:
            raise serializers.ValidationError({'Username': 'Username must have more then 2 character or less then 30'})
        return username
        
    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username']      
            )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'Password': 'Password must match'})
        if len(password) < 6 or len(password) > 16:
            raise serializers.ValidationError({'Password': 'Password must be longer than 4 characters'})

        user.set_password(password)
        user.save()
        return user

class PasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(style={'input_type': 'password'}, required=True)
    new_password = serializers.CharField(style={'input_type': 'password'}, required=True)
    
    def validate_current_password(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError({'current_password': 'Does not match'})
        raise value

class ProfilesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = (
                    #Function
                    'get_email', 'get_online_status'
                  )
