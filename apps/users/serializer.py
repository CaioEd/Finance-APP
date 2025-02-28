from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}   # Prevent password from being exposed in API responses.

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user