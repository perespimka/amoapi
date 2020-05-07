from django.db import models

# Create your models here.
class Leads(models.Model):
    amo_lead_id = models.IntegerField(unique=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'leads'

class Paints(models.Model):
    name = models.CharField(max_length=255)
    product = models.CharField(max_length=45)
    basis = models.CharField(max_length=45)
    catalog = models.CharField(max_length=45)
    code = models.CharField(max_length=45)
    shine = models.CharField(max_length=45)
    facture = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'paints'

class PaintsLeads(models.Model):
    paint = models.ForeignKey(Paints, on_delete=models.CASCADE)
    lead = models.ForeignKey(Leads, on_delete=models.CASCADE)
    date_add = models.CharField(max_length=45, blank=True, null=True)
    temperature = models.CharField(max_length=45, blank=True, null=True)
    applying = models.CharField(max_length=45, blank=True, null=True)
    postforming = models.CharField(max_length=45, blank=True, null=True)
    metallic = models.IntegerField(blank=True, null=True)
    chameleon = models.IntegerField(blank=True, null=True)
    antibacterial = models.IntegerField(blank=True, null=True)
    antigraffiti = models.IntegerField(blank=True, null=True)
    architect = models.IntegerField(blank=True, null=True)
    zinc = models.IntegerField(blank=True, null=True)
    client_sample = models.CharField(max_length=45, blank=True, null=True)
    comment = models.CharField(max_length=45, blank=True, null=True)
    potential_vol = models.IntegerField(blank=True, null=True)
    kp_price = models.IntegerField(blank=True, null=True)
    vol = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    delivery_date = models.CharField(max_length=45, blank=True, null=True)
    delivery_terms = models.CharField(max_length=45, blank=True, null=True)
    product_type = models.CharField(max_length=45, blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    reason = models.CharField(max_length=45, blank=True, null=True)
    surface = models.CharField(max_length=45, blank=True, null=True)
    panels = models.IntegerField(blank=True, null=True)
    powder = models.CharField(max_length=10, blank=True, null=True)
    surface_type = models.CharField(max_length=45, blank=True, null=True)
    surface_thin = models.CharField(max_length=45, blank=True, null=True)
    ntime_applying = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'paints_leads'