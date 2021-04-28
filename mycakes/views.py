from django.shortcuts import render
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from mycakes.serializers import AddCakeSerializer
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from mycakes.models import *
from mycakes.models import Cakes
from rest_framework.generics import RetrieveDestroyAPIView, RetrieveUpdateAPIView, ListCreateAPIView, ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView,UpdateAPIView


def response_generator(data, message, status):
    return{'data': data, 'message':message,'status':status}


class SearchCakes(APIView):
    def get(self, request, cakename):
        # cakes={}
        cake = Cakes.objects.filter(name=cakename)
        print('cake', cake)
        serializer = AddCakeSerializer(cake,many=True, context={'request': request})
        # cakes = response_generator(data=cake, message='success', status=201)
        return Response(response_generator(data=serializer.data, message='success', status=201), status=status.HTTP_201_CREATED)


class CakeDetails(RetrieveAPIView):
    queryset = Cakes.objects.all()
    serializer_class = AddCakeSerializer


class CakeDestroyView(DestroyAPIView):
    queryset = Cakes.objects.all()


class AddCakes(APIView):
    def post(self, request):
        data = request.data
        # print(data)
        serializer = AddCakeSerializer(data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(response_generator(data=serializer.data, message='success', status=201), status=status.HTTP_201_CREATED)
        print('formm',serializer.data)
        return Response(response_generator(data=serializer.data, message='error', status=400),  status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        posts = Cakes.objects.all()
        serializer = AddCakeSerializer(posts, many=True, context={'request': request})

        return Response(response_generator(data=serializer.data, message='success', status=201))
