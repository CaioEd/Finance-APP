from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}   # Prevent password from being exposed in API responses.

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    

# Novo serializer para JWT token customizado
# Adiciona informações personalizadas ao payload do token JWT.
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Adicionar dados personalizados ao token
        token['username'] = user.username
        token['email'] = user.email
        token['first_name'] = user.first_name
        return token