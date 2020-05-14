from django.core.mail import EmailMessage
from django.core.mail.backends.smtp import EmailBackend
import time
from .models import Leads, Paints, PaintsLeads
from .serializers import PaintsLeadsSerializer, PaintsLeadsSerializerLink, PaintsSerializer, PaintsSerializerLink, PaintsLeadsSerializerEdit
from .serializers import PaintsLeadsEmailSerializer
import logging
from django.http import HttpResponse
from .serializers import PaintsFullSerializer, PaintsLeadsFullSerializer
from django.db.models import Q
from docxtpl import DocxTemplate

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

def combine_paint_data(pl, PlSerializator, PSerializator):
    '''Возвращает словарь объединенный paints и paints_leads'''
    serializer_pl = PlSerializator(pl).data
    serializer_p = PSerializator(pl.paint).data
    serializer_p.update(serializer_pl)
    return serializer_p

def tag_creating(pl):
    res_string = f'{pl.paint.product} {pl.paint.catalog}{pl.paint.code}'
    if pl.product_type == 'sample':
        res_string = f'Образец {res_string}' 
    return res_string

def add_new_lead_id(pl, dict_to_add):
    new_id = pl.new_lead.amo_lead_id
    dict_to_add['new_lead_id'] = new_id

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
            combined = combine_paint_data(pl, PaintsLeadsSerializer, PaintsSerializer)
            if pl.new_lead:
                combined['new_lead_id'] = pl.new_lead.amo_lead_id
            else:
                combined['new_lead_id'] = None
            combined['tag'] = tag_creating(pl)
            serializer.append(combined)
        
    else:
        serializer = 'none' # На фронте так надо. Там ждут именно строку 'none', а не json'овский null
    result = {
        'id': lead.id,
        'amo_lead_id': lead.amo_lead_id,
        'sum': sum_,
        'lead_paints_info': serializer
    }
    return result

def set_status(pl, req):
    if req['product_type'] == 'sample':
        pl.status = 1
    elif req['product_type'] == 'paint':
        pl.status = 0

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
        logging.debug(req)
        if serialize_p.is_valid():
            name = get_paint_name(req)
            try:
                paint = Paints.objects.get(name=name, product=serialize_p.validated_data['product'], basis=serialize_p.validated_data['basis'],
                                           catalog=serialize_p.validated_data['catalog'], code=serialize_p.validated_data['code'], shine=serialize_p.validated_data['shine'],
                                           facture=serialize_p.validated_data['facture']
                )
            except:
                paint = serialize_p.save(name=name)
        else:
            logging.debug(serialize_p.errors)
        try:
            lead = Leads.objects.get(amo_lead_id=req['lead_id'])
        except:
            lead = Leads(amo_lead_id=req['lead_id']) 
            lead.save()
        serialize_pl = PaintsLeadsSerializerLink(data=req)
        if serialize_pl.is_valid():
            serialize_pl.save(lead=lead, paint=paint)
        else:
            logging.debug(serialize_pl.errors)
        
        pls = lead.paintsleads_set.all() # Все записи в paints_leads у текущего лида
        result = []
        for pl in pls:
            res_string = f'{pl.paint.product} {pl.paint.catalog}{pl.paint.code}'
            if pl.product_type == 'sample':
                res_string = f'Образец {res_string}'            
            result.append(res_string)      
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
    '''
    Редактирование краски
    '''
    if all((req['lead_id'], req['paints_leads_id'])):
        name = get_paint_name(req)
        serializer_p = PaintsSerializerLink(data=req)
        logging.debug(req)
        if serializer_p.is_valid():
            try:
                paint = Paints.objects.get(name=name, product=req['product'], basis=req['basis'],
                                           catalog=req['catalog'], code=req['code'], 
                                           shine=req['shine'], facture=req['facture']
                                           
                )
            except:
                paint = serializer_p.save(name=name)
        else:
            logging.debug(serializer_p.errors)
        lead = Leads.objects.get(amo_lead_id=req['lead_id'])
        try:
            pl = PaintsLeads.objects.get(id=req['paints_leads_id']) #!!!
        except:
            return {'status': 'omg  paints_leads id not found'}
        serializer_pl = PaintsLeadsSerializerEdit(pl, data=req)
        if serializer_pl.is_valid():
            serializer_pl.save(paint=paint)
        else:
            logging.debug(serializer_pl.errors)
        result = []
        for pl in lead.paintsleads_set.all():
            res_string = f'{pl.paint.product} {pl.paint.catalog}{pl.paint.code}'
            if pl.product_type == 'sample':
                res_string = f'Образец {res_string}'
            result.append(res_string)
        result = ','.join(result)
        return {'status': 'done', 'tags': result}

def get_paint_info(req):
    '''
    Данные по краске. Запрос на /paints
    '''
    if 'paints_leads_id' in req:
        try:
            pl = PaintsLeads.objects.get(id=req['paints_leads_id'])
        except:
            return {'status': 'paints_leads_id not found'}

        return combine_paint_data(pl, PaintsLeadsFullSerializer, PaintsFullSerializer)
    elif 'paint_id' in req:
        try:
            paint = Paints.objects.get(id=req['paint_id'])
        except:
            return {'status': 'paint_id not found'}
        return PaintsFullSerializer(paint).data

def paint_search(req):
    '''
    ПОиск краски. 
    '''
    query = req['query']
    q = (
        Q(name__icontains=query) | Q(product__icontains=query) | Q(basis__icontains=query) | Q(catalog__icontains=query) |
        Q(code__icontains=query) | Q(shine__icontains=query) | Q(facture__icontains=query)
    )
    result = []
    for paint in Paints.objects.filter(q):
        result.append({'id': paint.id, 'name': paint.name})
    return result
#*******   

def sample_data_to_xlsx(paints_to_xlsx):
    '''
    Создаем файл xlsx с данными образца для отправки в лабораторию
    Возвращаем имя файла
    '''
    import pandas as pd
    df_sample_data = pd.DataFrame(paints_to_xlsx)
    str_time = str(int(time.time()*1000)) + '.xlsx'
    fname = 'mail_files/' + str_time 
    df_sample_data.to_excel(fname, index=None)
    return fname



def send_mail_to(req, emails, attach, subject, body):
    import base64

    #sample_data = data['sample_data'].copy()
    manager_mail = base64.b64decode(req['manager_mail'].encode()).decode('utf-8')
    manager_mail_pass = base64.b64decode(req['manager_mail_pass'].encode()).decode('utf-8')
    #attach = sample_data_to_xlsx(sample_data)
    em = EmailMessage(subject=subject, body=body,
                      to=emails, from_email=manager_mail
    )

    em.attach_file(attach)
    EmailBackend(
        host = 'mail.stardustpaints.ru',
        username = manager_mail,
        password = manager_mail_pass,
        #use_ssl = True,
        use_tls = True,
        port = 587
    ).send_messages([em])    

def send_mail_to_lab_prod(req):
    if req['state'] == 'send_lab':
        emails = ['s.dmitrievlol@yandex.ru', 'soloviev357@gmail.com'] # Изменить на лабу
        status_value = 1
    else:
        emails = ['s.dmitrievlol@yandex.ru', 'soloviev357@gmail.com'] # Изменить на бэкофис
        status_value = 2
    new_lead = Leads(amo_lead_id=req['new_id'])
    try:
        new_lead.save()
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    paints_to_xlsx = []
    for pl_id in req['id']:
        pl = PaintsLeads.objects.get(id=pl_id)
        pl.status = status_value
        pl.new_lead = new_lead
        pl.save()
        pl.id = None
        pl.lead = new_lead
        pl.new_lead = None
        pl.save()
        paints_to_xlsx.append(combine_paint_data(pl, PaintsLeadsEmailSerializer, PaintsFullSerializer))
    attach = sample_data_to_xlsx(paints_to_xlsx)
    send_mail_to(req, emails, attach, 'Создать образец', 'Просьба создать образец, данные во вложении')
    
def email_from_contacts(req):
    contacts = req['data_manager']['man_comp_users']
    for contact in contacts:
        email = contact.get('email')
        if email:
            return email, contact.get('name'), contact.get('position')




def send_cp(req):
    context = {}
    contacts = email_from_contacts(req)
    if contacts:
        email, context['fio_from_card'], context['position'] = contacts
        context['company_name'] = req['data_manager']['man_comp_name']
        context['manager_name'] = req['data_manager']['man_name'] + ' ' + req['data_manager']['man_last_name']
        context['manager_email'] = req['data_manager']['man_login']
        context['manager_phone'] = req['data_manager']['man_phone_number']
        context['tbl'] = []
        for pl_id in req['id']:
            pl_table = {}
            pl = PaintsLeads.objects.get(id=int(pl_id))
            pl_table['name'] = (f'{pl.paint.catalog} {pl.paint.code} {pl.paint.basis} {pl.paint.facture} '
                                f'{pl.paint.shine}, применение {pl.applying}'
            )
            pl_table['vol'] = str(pl.vol)
            pl_table['price'] = str(pl.price)
            context['tbl'].append(pl_table)
        doc = DocxTemplate('/home/perespimka/monyze/cp_stardustpaints.docx')
        doc.render(context)
        now = time.strftime('%d-%m-%Y', time.localtime())
        fname = f'mail_files/cp_to_{context["company_name"].lower()}_{now}.docx'
        doc.save(fname)
        
        send_mail_to(req, ['s.dmitrievlol@yandex.ru', 'soloviev357@gmail.com'], fname,
                     'Коммерческое предложение Stardustpaints', 'Добрый день! Коммерческое предложение во вложении.'   
        )



      
        
    
    


if __name__ == "__main__":
    print(name_switch('RAL'))