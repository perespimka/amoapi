from .models import Leads, Paints, PaintsLeads
from .serializers import PaintsLeadsSerializer, PaintsLeadsSerializerLink, PaintsSerializer, PaintsSerializerLink
import logging
from django.http import HttpResponse

logging.basicConfig(level=logging.DEBUG, filename='/home/perespimka/monyze/log.txt', format='%(asctime)s %(levelname)s %(message)s')
NAME_SWITCH = {
    "ral": "RAL",
    "ral design": "RALD",
    "ral classic": "RALC",
    "ral effect": "RALE",
    "nsc": "NCS",
    "pantone": "PNT",
    "Глянцевая 80-100%": "80/100%",
    "Полулянцевая 55-80%": "55/80%", 
    "Полуматовая 30-55%": "30/55%",
    "Матовая 15-30%": "15/30%",
    "Суперматовая 1-15%": "1-15%", 
    "Шагрень": "шгр",
    "Гладкая": "гл",
    "Антик": "ант",
    "Муар": "мр",
    "Молотковая": "мтк",
    "Шелк": "шлк",
    "Не определено": "н/о",
    }


def get_lead_data(req):
    try:
        lead = Leads.objects.get(amo_lead_id=req['lead_id'])
    except Leads.DoesNotExist:
        lead = Leads(amo_lead_id=req['lead_id'])
        lead.save()
    paints_leads = lead.paintsleads_set.all()
    sum_ = 0
    serializer = []
    if len(paints_leads) > 0:
        for pl in paints_leads:
            try:
                sum_ += pl.price * pl.vol # Тут уточнить по обязательности заполнения полей
            except:
                pass
            paint = PaintsSerializer(pl.paint).data
            pl_serz = PaintsLeadsSerializer(pl).data
            pl_serz.update(paint)
            serializer.append(pl_serz)
        
    else:
        serializer = 'none' # На фронте так надо. Там ждут именно строку 'none', а не json'овский null
    result = {
        'id': lead.id,
        'amo_lead_id': lead.amo_lead_id,
        'sum': sum_,
        'lead_paints_info': serializer
    }
    return result

def name_switch(name):
    if name in NAME_SWITCH:
        return NAME_SWITCH[name]
    return name


def attach_goods(req):
    if req['product_type'] == 'sample' and all((req['product'], req['basis'], req['catalog'], req['code'], req['shine'], req['facture'])):
        serialize_p = PaintsSerializerLink(data=req)
        if serialize_p.is_valid():
            name = (name_switch(req['catalog']) + req['code'] + '-' + req['basis'] + '-' + name_switch(req['shine']) +
                    '-' + name_switch(req['facture'])
            ) 
            try:
                paint = Paints.objects.get(name=name, product=req['product'], basis=req['basis'],
                                           catalog=req['catalog'], code=req['code'], shine=req['shine'],
                                           facture=req['facture']
                )
            except:
                paint = serialize_p.save(name=name)
          

        try:
            lead = Leads.objects.get(amo_lead_id=req['lead_id'])
        except:
            lead = Leads(amo_lead_id=req['lead_id']) #Уточнить, устроит ли такое
            lead.save()
        serialize_pl = PaintsLeadsSerializerLink(data=req)
        if serialize_pl.is_valid():
            serialize_pl.save(lead=lead, paint=paint)
        pls = lead.paintsleads_set.all() # Все записи в paints_leads у текущего лида
        result = []
        for pl in pls:
            result.append(f'Образец {pl.paint.product} {pl.paint.catalog}{pl.paint.code}')      
        result = ','.join(result)

        return {'status': 'done', 'tags': result}

if __name__ == "__main__":
    print(name_switch('RAL'))