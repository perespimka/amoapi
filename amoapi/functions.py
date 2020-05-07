from .models import Leads
from .serializers import PaintsLeadsSerializer


def get_lead_data(req):
    try:
        lead = Leads.objects.get(amo_lead_id=req['lead_id'])
    except Leads.DoesNotExist:
        lead = Leads(amo_lead_id=req['lead_id'])
        lead.save()
    paints_leads = lead.paintsleads_set.all()
    sum_ = 0
    if len(paints_leads) > 0:
        for pl in paints_leads:
            try:
                sum_ += pl.price * pl.vol # Тут уточнить по обязательности заполнения полей
            except:
                pass
        serializer = PaintsLeadsSerializer(paints_leads, many=True).data
    else:
        serializer = 'none' # На фронте так надо. Там ждут именно строку 'none', а не json'овский null
    result = {
        'id': lead.id,
        'amo_lead_id': lead.amo_lead_id,
        'sum': sum_,
        'lead_paints_info': serializer
    }
    return result

