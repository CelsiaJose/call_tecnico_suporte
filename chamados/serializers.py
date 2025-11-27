from rest_framework import serializers
from .models import Chamados
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id', 'username', 'email']


class ChamadoSerializer(serializers.ModelSerializer):
    # Quero que o usuario apenas sejam lidos nao criados ,eles são criados no servidor 
    usuario=UserSerializer(read_only=True)
    tecnico=UserSerializer(read_only=True)
    class Meta:
        model=Chamados
        fields='__all__'






