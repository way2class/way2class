from rest_framework import serializers
from .models import User  # your custom user model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "is_staff", "is_active"]  
