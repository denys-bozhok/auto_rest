from rest_framework import serializers

from . import models


class SerializedAuto(serializers.ModelSerializer):
    class Meta:
        model = models.Auto
        fields = ['label', 'year', 'price', 'description', 'slug',]
       
        
class SerializedAutoPassport(serializers.ModelSerializer):
    class Meta:
        model = models.AutoPassport
        fields = ['related_auto', 'number', 'prefix',]
        
        
class SerializedOwner(serializers.ModelSerializer):
    class Meta:
        model = models.Owner
        fields = ['first_name', 'last_name', 'car_number',]