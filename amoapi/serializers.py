from rest_framework import serializers
from .models import Leads, Paints, PaintsLeads, MailPass
import json
import logging

logging.basicConfig(level=logging.DEBUG, filename='/home/perespimka/monyze/log.txt', format='%(asctime)s %(levelname)s %(message)s')

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
    status_sample = serializers.ListField(required=False)
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
    status_sample = serializers.ListField(required=False)
    class Meta:
        model = PaintsLeads
        fields = ('id', 'temperature', 'applying', 'postforming', 'metallic', 'chameleon', 'antibacterial', 
                  'antigraffiti', 'architect', 'zinc', 'client_sample', 'comment', 'status', 'reason', 'surface', 'panels', 'powder', 'product_type', 
                  'surface_type', "surface_thin", "delivery_date", "delivery_terms", "vol", "price", 'ntime_applying',
                  "status_sample", 'paid_sample', 'sublim'

        )

#Full
class PaintsLeadsFullSerializer(serializers.ModelSerializer):
    status_sample = serializers.SerializerMethodField() #ListField некорректно сериализовал объект, выдавая список из букв. 


    class Meta:
        model = PaintsLeads
        fields = ('__all__')
        #exclude = ('lead', 'paint', 'date_add')
    def get_status_sample(self, obj):

        obj = obj.status_sample   
        if obj:    
            obj = obj.replace("'", '"')
            res = json.loads(obj)
            return res
        else:
            return None
class PaintsFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paints
        fields = ('__all__')
        #exclude = ('id',)

#ForEmail
class PaintsLeadsEmailSerializer(serializers.ModelSerializer):
    status_sample = serializers.ListField(required=False)
    class Meta:
        model = PaintsLeads
        #fields = ('__all__')
        exclude = ('id', 'lead', 'paint', 'date_add', 'new_lead'  )

class MailPassSer(serializers.ModelSerializer):
    status_sample = serializers.ListField(required=False)
    class Meta:
        model = MailPass
        fields = ('__all__')