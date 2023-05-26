from rest_framework import serializers

from .models import About


class AboutListSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['title', 'content', 'slug']

class AboutCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['title', 'content']
        
class AbutUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['title', 'content']
        
    def update(self, instance, validated_data):
        instance.title = validated_data.get['title', instance.title]
        instance.content = validated_data.get['content', instance.content]
        instance.save()
        return instance
