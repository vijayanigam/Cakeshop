from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from authenticate.serializers import  UserSerializer
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from usercakes.models import UserDetails
from usercakes.serializers import UserDetailsSerializer


def response_generator(data, message, status):

    return{'data': data, 'message':message,'status':status}


class Register(APIView):
    def post(self, request):
        data = request.data
        print(data)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            Logindone(serializer.data)
            return Response(response_generator(data=serializer.data, message='success', status=201), status=status.HTTP_201_CREATED)
        return Response(response_generator(data=serializer.data, message='error', status=400), status=status.HTTP_400_BAD_REQUEST)


def Logindone(data):
    print(data)

    user_ = UserDetails(email=data['email'])
    user_.save()
    print(user_)


    return 1

# class Logindone(APIView):
#     def (self,request):
#         user = self.context['request'].user
#         print(user)
#         # print(request.auth)
#         return HttpResponse("Your response")