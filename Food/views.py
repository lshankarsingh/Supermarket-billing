from django.shortcuts import render
from rest_framework import serializers

from Book.serializer import FoodSerializer
#from serializer import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def Foodcategory(request):
    booksobj=Productslist.objects.all()
    serializer=FoodSerializer(booksobj,many=True)
    print(serializer)
    return Response(serializer.data) 
'''
#Create
@api_view(['POST'])
def post_Book(request):
    booksobj=Productslist.objects.all()
    serializer=FoodSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#update
@api_view(['POST'])
def update_Book(request,id):
    booksobj=Productslist.objects.get(id=id)
    serializer=FoodSerializer(instances=booksobj,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)'''