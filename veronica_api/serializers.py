from django.contrib.auth.models import User, Group
from rest_framework import serializers
from veronica_api.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class AlumnoSerializer(serializers.ModelSerializer):
    user_username = serializers.ReadOnlyField(source='user.username', read_only=True)
    user_email = serializers.ReadOnlyField(source='user.email', read_only=True)
    user_is_superuser = serializers.ReadOnlyField(source='user.is_superuser', read_only=True)
    class Meta:
        model = Alumno
        fields = (
            'url',
            'nombre',
            'cedula',
            'user_username',
            'user_email',
            'user_is_superuser',
        )
