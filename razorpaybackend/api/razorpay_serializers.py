from rest_framework import serializers
from razorpaybackend.models import Transaction

class CreateOrderSerializer(serializers.Serializer):
    amount = serializers.IntegerField()
    currency = serializers.CharField()
    
    
class TransactionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Transaction
        fields = ['order_id','payment_id','signature']
        

from payments.models import Transaction

class BuyProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Transaction
        fields = ['id','buyer','order_id','payment_id','signature','seller','food_item_id','food_item_name','quantity','amount','status']

        