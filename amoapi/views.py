from django.shortcuts import render
from django.http import HttpResponse
import logging
from rest_framework.decorators import api_view
from .functions import get_lead_data, attach_goods, del_paintsleads_rec, edit_paint, get_paint_info, paint_search, send_mail_to_lab_prod, send_cp
from .tokenz import api_key
from .models import Leads
from rest_framework.response import Response
from .serializers import PaintsLeadsSerializer

logging.basicConfig(level=logging.DEBUG, filename='/home/perespimka/monyze/log.txt', format='%(asctime)s %(levelname)s %(message)s')

# Create your views here.
@api_view(['POST'])
def send_email(request):
    #logging.debug('request:')
    #logging.debug(request.content_type)
    #logging.debug(request.data)
    if request.data['state'] == 'send_lab' or request.data['state'] == 'send_prod' or request.data['state'] == 'set_score':
        send_mail_to_lab_prod(request.data)
        #send_mail_to(request.data)
    if request.data['state'] == 'send_cp':
        send_cp(request.data)
        logging.debug(request.data)
       
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


