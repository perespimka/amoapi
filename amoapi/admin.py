from django.contrib import admin
from .models import Leads, PaintsLeads, Paints, MailPass

# Register your models here.
admin.site.register(Leads)
admin.site.register(PaintsLeads)
admin.site.register(Paints)
admin.site.register(MailPass)
