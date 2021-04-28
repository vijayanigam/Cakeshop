from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from usercakes.serializers import UserDetailsSerializer, PlaceOrderSerializer
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from mycakes.models import *
from usercakes.models import UserDetails, Order
from rest_framework.generics import RetrieveDestroyAPIView, RetrieveUpdateAPIView, ListCreateAPIView, ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView,UpdateAPIView
import json
from mycakes.models import Cakes
from mycakes.serializers import AddCakeSerializer
from rest_framework.generics import RetrieveDestroyAPIView, RetrieveUpdateAPIView, ListCreateAPIView, ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView,UpdateAPIView
from .serializers import *


class OrderRetrieveView(APIView):
    def post(self,request):
        order = []
        data = request.data
        orders = Order.objects.filter(email=data['email'])
        # print(orders.cakes.all())
        serializer = PlaceOrderSerializer(orders, many=True)
        # print(serializer.data)
        for i in serializer.data:
            a = []
            for j in i['cakes']:
                # print(i['cakes'])
                # print('j', j)
                c = Cakes.objects.get(cakeid=j)
                a.append(c)
            serializer1 = AddCakeSerializer(a, context={'request': request}, many=True)
            print(serializer1.data)
            result = response_generator(i, serializer1.data)
            print(result)
            order.append(result)
        print('order', order)
        cake = UserDetails.objects.get(email=data['email'])
        id = cake.cart.all()
        cake.cart.clear()
        print('after',id)
        # my_object.relations.clear()
        return Response(order)


def response_generator(order,cakes):
    print(order,'**********')
    for data in order:
        if data == 'cakes':
            print(order[data])
            for cake in range(len(order[data])):
                print(order[data][cake])
                order[data][cake] = cakes[cake]
                print(cakes[cake])
            print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    return order


class PlaceOrder(APIView):
    def post(self,request):
        data = request.data
        print(data, 'email&&&&&&&&&&')
        cart = UserDetails.objects.get(email=data['email'])
        # print(cart)
        id = cart.cart.all()
        serializer = PlaceOrderSerializer(data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data['id'])
            obj = Order.objects.get(id=serializer.data['id'])
            for i in id:
                print('cakeid', i.cakeid)
                obj.cakes.add(Cakes.objects.get(cakeid=i.cakeid))
            # obj.cakes = cart.cart
            print('saved')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class AddToCart(APIView):
    def put(self, request, pk):
        data = request.data
        print(data['email'], 'email&&&&&&&&&&')
        cake = UserDetails.objects.get(email=data['email'])
        id = cake.cart.all()
        cake.cart.add(Cakes.objects.get(cakeid=pk))
        print(cake, id)
        data = cake.cart.all()
        serializer = UserDetailsSerializer(cake, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response('serializer.data', status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RemoveFromCart(APIView):
    def post(self, request):
        data = request.data
        print(data['email'], 'email&&&&&&&&&&')
        cake = UserDetails.objects.get(email=data['email'])
        id = cake.cart.all()
        cake.cart.remove(Cakes.objects.get(cakeid=data['cakeid']))
        print(cake, id)
        data = cake.cart.all()
        serializer = UserDetailsSerializer(cake,  partial=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
# my_mood.interests.remove(my_interest)


class GetCart(APIView):
    def post(self, request):
        a = []
        # print(request.headers)
        data = request.data
        print('-----------', data)
        cake = UserDetails.objects.get(email=data['email'])
        id = cake.cart.all()
        serializer = UserDetailsSerializer(cake, context={'request': request})
        for i in serializer.data['cart']:
            print(i, 'id')
            c = Cakes.objects.get(cakeid=i)
            a.append(c)
        print(a)
        serializer1 = AddCakeSerializer(a, context={'request': request}, many=True)
        # print(serializer1)
        return Response(serializer1.data)




