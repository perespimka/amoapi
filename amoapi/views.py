from django.shortcuts import render
from django.http import HttpResponse
import logging
from rest_framework.decorators import api_view
from django.core.mail import EmailMessage
from django.core.mail.backends.smtp import EmailBackend
import time
from .functions import get_lead_data, attach_goods, del_paintsleads_rec, edit_paint, get_paint_info, paint_search
from .tokenz import api_key
from .models import Leads
from rest_framework.response import Response
from .serializers import PaintsLeadsSerializer

logging.basicConfig(level=logging.DEBUG, filename='/home/perespimka/monyze/log.txt', format='%(asctime)s %(levelname)s %(message)s')


def prepare_dict_to_DF(sample_data):
    '''Заменим значения на списки, содержащие эти значения, для создания DataFrame'''
    for key in list(sample_data):
        logging.debug('++++++++'*3)
        logging.debug(sample_data[key])
        sample_data[key] = [sample_data[key]]
        logging.debug(sample_data[key])
        logging.debug('--------'*3)

def sample_data_to_xlsx(sample_data):
    '''
    Создаем файл xlsx с данными образца для отправки в лабораторию
    Возвращаем кортеж для отправки в EmailMessage: имя файла, бинарник, тип контента
    '''
    import pandas as pd

    prepare_dict_to_DF(sample_data)
    df_sample_data = pd.DataFrame(sample_data)
    str_time = str(int(time.time()*1000)) + '.xlsx'
    fname = 'mail_files/' + str_time 
    df_sample_data.to_excel(fname, index=None)
    return fname

def send_mail_to_lab(data):
    import base64

    mails = ['s.dmitrievlol@yandex.ru', 'soloviev357@gmail.com', 'ts@stardustpaints.ru']
    sample_data = data['sample_data'].copy()
    manager_mail = base64.b64decode(data['manager_mail'].encode()).decode('utf-8')
    manager_mail_pass = base64.b64decode(data['manager_mail_pass'].encode()).decode('utf-8')
    attach = sample_data_to_xlsx(sample_data)
    em = EmailMessage(subject='Создать образец', body='Просьба создать образец, данные во вложении',
                      to=mails, from_email=manager_mail
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
    
    #em.send()


# Create your views here.
@api_view(['POST'])
def send_email(request):
    logging.debug('request:')
    logging.debug(request.content_type)
    logging.debug(request.data)
    if request.data['state'] == 'send_lab' or request.data['state'] == 'send_prod':
        send_mail_to_lab(request.data)

    return HttpResponse('<h1>Ok boomer</h1>')


@api_view(['POST'])
def leads(request):
    req = request.data
    if not api_key == req['api_key']:
        return HttpResponse('<h1>Nice try :D</h1>')
    if req['request_from'] == 'amo':
        # Даем инфо по лиду
        if req['state'] == 'get_lead_info':
            result = get_lead_data(req)
            return Response(result)
        elif req['state'] == 'add_lead':
            lead = Leads(amo_lead_id=req['lead_id'])
            lead.save()
            return HttpResponse('done') # Так хотят на фронте
        elif req['state'] == 'link' and req['lead_id'] and req['product_type']:
            result = attach_goods(req)
            logging.debug(result)
            return Response(result)
        elif req['state'] == 'unlink':
            return Response(del_paintsleads_rec(req))
        elif req['state'] == 'edit':
            return Response(edit_paint(req))
    return HttpResponse('lalala')

@api_view(['POST'])
def paints(request):
    req = request.data
    if not api_key == req['api_key']:
        return HttpResponse('<h1>Nice try :D</h1>')
    if req['request_from'] == 'amo':
        if req['state'] == 'get_paint_info':
            return Response(get_paint_info(req))
        if req['state'] == 'search' and len(req['query']) >= 2:
            return Response(paint_search(req))

