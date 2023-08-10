from rest_framework import serializers
from .models import GeekUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeekUser
        fields = '__all__'
