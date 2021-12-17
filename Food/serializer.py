from django.db.models import fields
from rest_framework import serializers
from .models import Productslist

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model=Productslist
        fields=('name','category','subcategory','amount')