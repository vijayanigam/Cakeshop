from django.contrib.auth.models import User
from django.db import models
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from mycakes.models import Cakes


class AddCakeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cakes
        fields = '__all__'

