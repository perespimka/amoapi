from rest_framework import serializers
from .models import Leads, Paints, PaintsLeads, MailPass


# Сериализаторы для get_lead_inf
class PaintsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paints
        fields = ('name', )


class PaintsLeadsSerializer(serializers.ModelSerializer):
    date_add = serializers.DateTimeField(format='%d-%m-%Y', read_only=True)
    class Meta:
        model = PaintsLeads
        fields = ('id', 'product_type', 'date_add',  'price',  'vol', 'status',  )
    
#Для link
class PaintsSerializerLink(serializers.ModelSerializer):
    class Meta:
        model = Paints
        fields = ('product', 'basis', 'catalog', 'code', 'shine', 'facture')

class PaintsLeadsSerializerLink(serializers.ModelSerializer):

    class Meta:
        model = PaintsLeads
        fields = ('temperature', 'applying', 'postforming', 'metallic', 'chameleon', 'antibacterial', #"potential_vol", "kp_price",
                  'antigraffiti', 'architect', 'zinc', 'client_sample', 'comment', 'status', 'reason', 'surface', 'panels', 'powder', 'product_type',
                  'surface_type', "surface_thin", "delivery_date", "delivery_terms", "vol", "price", 'ntime_applying',
                  "status_sample", 'paid_sample', 'sublim'
        )
# Edit
class PaintsLeadsSerializerEdit(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = PaintsLeads
        fields = ('id', 'temperature', 'applying', 'postforming', 'metallic', 'chameleon', 'antibacterial', 
                  'antigraffiti', 'architect', 'zinc', 'client_sample', 'comment', 'status', 'reason', 'surface', 'panels', 'powder', 'product_type', 
                  'surface_type', "surface_thin", "delivery_date", "delivery_terms", "vol", "price", 'ntime_applying',
                  "status_sample", 'paid_sample', 'sublim'

        )

#Full
class PaintsLeadsFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaintsLeads
        fields = ('__all__')
        #exclude = ('lead', 'paint', 'date_add')

class PaintsFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paints
        fields = ('__all__')
        #exclude = ('id',)

#ForEmail
class PaintsLeadsEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaintsLeads
        #fields = ('__all__')
        exclude = ('id', 'lead', 'paint', 'date_add', 'new_lead'  )

class MailPassSer(serializers.ModelSerializer):
    class Meta:
        model = MailPass
        fields = ('__all__')