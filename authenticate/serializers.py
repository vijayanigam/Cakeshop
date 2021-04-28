from django.contrib.auth.models import User
from django.db import models
from rest_framework.validators import UniqueValidator
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=8)

    def create(self, validate_data):
        user = User.objects.create_user(validate_data['username'],validate_data['email'],  validate_data['password'])
        return user

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

