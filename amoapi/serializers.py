from rest_framework import serializers
from .models import Leads, Paints, PaintsLeads

class PaintsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paints
        fields = ('name', )


class PaintsLeadsSerializer(serializers.ModelSerializer):
    paint_data = PaintsSerializer(read_only=True)
    class Meta:
        model = PaintsLeads
        fields = ('id', 'product_type', 'date_add', 'kp_price', 'price', 'potential_vol', 'vol', 'paint_data' )
    