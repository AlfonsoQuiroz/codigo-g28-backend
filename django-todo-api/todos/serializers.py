from rest_framework import serializers
from .models import Todo
from django.contrib.auth.models import User


class TodoSerializer(serializers.ModelSerializer):
    """
    Clase que simula ser el to_dict() de Flask
    """
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Todo
        fields = [
            'id',
            'title',
            'descrption',
            'category',
            'created_at',
            'user'
          ]
        read_only_fields = ['id', 'created_at', 'user']
