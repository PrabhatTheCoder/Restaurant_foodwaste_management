from datetime import timedelta
from rest_framework import serializers
from .models import RawMaterial, RestaurantMenu


class RawMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawMaterial
        fields = '__all__'
        

class ListRawMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawMaterial
        fields = ['id','name','image','weight','expired_at']
        
        
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantMenu
        fields = '__all__'
        
class NewMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantMenu
        fields = ['name','image','price_per_serving','serving_size','total_weight','client']
    
        
class ListMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantMenu
        fields = ['id','name','price_per_serving','image','total_weight','expired_at']

    
class DonateRestaurantMenuSerializer(serializers.ModelSerializer):
    menu_id = serializers.UUIDField()
    quantity = serializers.IntegerField()
    
    class Meta:
        model = RestaurantMenu
        fields = ['menu_id','quantity']

    
class DonateRawMaterialSerializer(serializers.ModelSerializer):
    rawMaterial_id = serializers.UUIDField()
    quantity = serializers.IntegerField()
    
    class Meta:
        model = RawMaterial
        fields = ['rawMaterial_id','quantity']
        
    
from rest_framework import serializers
from .models import Donation

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ['id','client','food_item_type','food_item_id','food_item_name','quantity', 'created_at']
        read_only_fields = ['id', 'created_at']



    
from payments.models import Transaction

class BuyRestaurantMenuSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Transaction
        fields = ['id','buyer','seller','food_item_id','food_item_name','quantity','price','transaction_id','status']
        

