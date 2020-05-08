from rest_framework import serializers
from .models import Leads, Paints, PaintsLeads


# Сериализаторы для get_lead_inf
class PaintsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paints
        fields = ('name', )


class PaintsLeadsSerializer(serializers.ModelSerializer):
    paint_data = PaintsSerializer(read_only=True, many=True)
    class Meta:
        model = PaintsLeads
        fields = ('id', 'product_type', 'date_add', 'kp_price', 'price', 'potential_vol', 'vol', 'paint_data' )
    
#Для link
class PaintsSerializerLink(serializers.ModelSerializer):
    class Meta:
        model = Paints
        fields = ('product', 'basis', 'catalog', 'code', 'shine', 'facture')

class PaintsLeadsSerializerLink(serializers.ModelSerializer):

    class Meta:
        model = PaintsLeads
        fields = ('temperature', 'applying', 'postforming', 'metallic', 'chameleon', 'antibacterial', 
                  'antigraffiti', 'architect', 'zinc', 'client_sample', 'comment', 'status', 'reason', 'surface', 'panels', 'powder', 'product_type' 
        )

class PaintsLeadsSerializerEdit(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = PaintsLeads
        fields = ('id', 'temperature', 'applying', 'postforming', 'metallic', 'chameleon', 'antibacterial', 
                  'antigraffiti', 'architect', 'zinc', 'client_sample', 'comment', 'status', 'reason', 'surface', 'panels', 'powder', 'product_type' 
        )
