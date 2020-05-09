from .models import Leads, Paints, PaintsLeads
from .serializers import PaintsLeadsSerializer, PaintsLeadsSerializerLink, PaintsSerializer, PaintsSerializerLink, PaintsLeadsSerializerEdit
import logging
from django.http import HttpResponse
from .serializers import PaintsFullSerializer, PaintsLeadsFullSerializer
from django.db.models import Q


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
    '''
    Возвращаем данные по сделке
    '''
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

def get_paint_name(req):
    return (name_switch(req['catalog']) + req['code'] + '-' + req['basis'] + '-' + name_switch(req['shine']) +
                    '-' + name_switch(req['facture'])
    )

def attach_goods(req):
    '''
    Запись краски и дополнительных данных в paints и paints_leads
    '''
    if all((req['product'], req['basis'], req['catalog'], req['code'], req['shine'], req['facture'])):
        serialize_p = PaintsSerializerLink(data=req)
        if serialize_p.is_valid():
            name = get_paint_name(req)
            try:
                paint = Paints.objects.get(name=name, product=serialize_p.validated_data['product'], basis=serialize_p.validated_data['basis'],
                                           catalog=serialize_p.validated_data['catalog'], code=serialize_p.validated_data['code'], shine=serialize_p.validated_data['shine'],
                                           facture=serialize_p.validated_data['facture']
                )
            except:
                paint = serialize_p.save(name=name)

        try:
            lead = Leads.objects.get(amo_lead_id=req['lead_id'])
        except:
            lead = Leads(amo_lead_id=req['lead_id']) 
            lead.save()
        serialize_pl = PaintsLeadsSerializerLink(data=req)
        if serialize_pl.is_valid():
            serialize_pl.save(lead=lead, paint=paint)
        pls = lead.paintsleads_set.all() # Все записи в paints_leads у текущего лида
        result = []
        for pl in pls:
            result.append(f'Образец {pl.paint.product} {pl.paint.catalog}{pl.paint.code}')      
        result = ','.join(result)

        return {'status': 'done', 'tags': result} # Так просит фронт 

def del_paintsleads_rec(req):
    '''
    Удаляем запись в paints_leads
    '''
    try:
        pl = PaintsLeads.objects.get(id=req['paints_leads_id'])
    except:
        return {'status': 'not ok'}
    pl.delete()
    lead = Leads.objects.get(amo_lead_id=req['lead_id'])
    result = []
    for pl in lead.paintsleads_set.all():
        res_string = f'{pl.paint.product} {pl.paint.catalog}{pl.paint.code}'
        result.append(res_string)
    result = ','.join(result)
    return {'status': 'done', 'tags': result}
    
def edit_paint(req):
    if all((req['lead_id'], req['paints_leads_id'])):
        name = get_paint_name(req)
        serializer_p = PaintsSerializerLink(data=req)
        if serializer_p.is_valid():
            try:
                paint = Paints.objects.get(name=name, product=serializer_p.validated_data['product'], basis=serializer_p.validated_data['basis'],
                                           catalog=serializer_p.validated_data['catalog'], code=serializer_p.validated_data['code'], 
                                           shine=serializer_p.validated_data['shine'], facture=serializer_p.validated_data['facture']
                                           
                )
            except:
                paint = serializer_p.save(name=name)
        lead = Leads.objects.get(amo_lead_id=req['lead_id'])
        try:
            pl = PaintsLeads.objects.get(id=req['paints_leads_id']) #!!!
        except:
            return {'status': 'omg  paints_leads id not found'}
        serializer_pl = PaintsLeadsSerializerEdit(pl, data=req)
        if serializer_pl.is_valid():
            serializer_pl.save(paint=paint)
        result = []
        for pl in lead.paintsleads_set.all():
            res_string = f'{pl.paint.product} {pl.paint.catalog}{pl.paint.code}'
            if pl.product_type == 'sample':
                res_string = f'Образец {res_string}'
            result.append(res_string)
        result = ','.join(result)
        return {'status': 'done', 'tags': result}

def get_paint_info(req):
    if req['paints_leads_id']:
        try:
            pl = PaintsLeads.objects.get(id=req['paints_leads_id'])
        except:
            return {'status': 'paints_leads_id not found'}
        paint = pl.paint
        serializer_pl = PaintsLeadsFullSerializer(pl)
        serializer_p = PaintsFullSerializer(paint)
        serializer_p.data.update(serializer_pl.data)
        return serializer_p.data
    elif req['paint_id']:
        try:
            paint = Paints.objects.get(id=req['paint_id'])
        except:
            return {'status': 'paint_id not found'}
        return PaintsFullSerializer(paint).data

def paint_search(req):
    query = req['query']
    q = (
        Q(name__icontains=query) | Q(product__icontains=query) | Q(basis__icontains=query) | Q(catalog__icontains=query) |
        Q(code__icontains=query) | Q(shine__icontains=query) | Q(facture__icontains=query)
    )
    result = []
    for paint in Paints.objects.filter(q):
        result.append({'id': paint.id, 'name': paint.name})
    return result
        

if __name__ == "__main__":
    print(name_switch('RAL'))