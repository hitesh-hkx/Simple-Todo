from rest_framework import serializers
from .models import Todo
from django.contrib.auth.models import User

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = [ 'id','text','complete']

class UserRegSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password',]
