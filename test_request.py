# -*- coding: utf-8 -*-

import requests
import base64
import logging


logging.basicConfig(level=logging.DEBUG, filename='log_test_request.txt', format='%(asctime)s %(levelname)s %(message)s')
URL = 'https://api.stardustpaints.ru/amoapi/send_email'
URL2 = 'https://api.stardustpaints.ru/amoapi/leads/'
URL3 = 'https://api.stardustpaints.ru/amoapi/paints/'

to_send = {
    'state': 'send_prod',
    'sample_data':{
        'testkey1': 'testval1',
        'testkey2': 2
    },
    'manager_mail': base64.b64encode('soloviev@stardustpaints.ru'.encode()).decode('utf-8'),
    'manager_mail_pass': base64.b64encode('33Kgtsl11'.encode()).decode('utf-8')
}

to_send_2 = {
    'api_key': 'Hvdtygevzr52unsrabsr5q1gA#a',
    'request_from': 'amo',
    'state': 'get_lead_info',
    'lead_id': 111,

}
to_send_3 = {
    "api_key": "Hvdtygevzr52unsrabsr5q1gA#a",
    "request_from": "amo",
    "state": "link",
    "lead_id": "111",
    "product_type": "sample",
    "name": "",
    "product": "KJKJKJ",
    "delivery_date": "",
    "delivery_terms": "Не определено",
    "potential_vol": "13",
    "kp_price": "13",
    "vol": "",
    "price": "",
    "basis": "PE",
    "catalog": "RAL",
    "code": "2215",
    "shine": "Не определено",
    "facture": "Гладкая",
    "temperature": "Стандарт",
    "postforming": 0,
    "applying": "Не определено",
    "surface_thin": "",
    "surface_type": "Не определено",
    "comment": "",
    "metallic": 0,
    "chameleon": 0,
    "antibacterial": 0,
    "antigraffiti": 0,
    "architect": 0,
    "zinc": 0
}
delete_pl = {
    'api_key': 'Hvdtygevzr52unsrabsr5q1gA#a',
    'request_from': 'amo',
    'state': 'unlink',
    'lead_id': 131,
    'paints_leads_id': 10
}

edit = {
    'paints_leads_id': 9,
    "api_key": "Hvdtygevzr52unsrabsr5q1gA#a",
    "request_from": "amo",
    "state": "edit",
    "lead_id": 111,
    "product_type": "sample",
    "name": "",
    "product": "Краска",
    "delivery_date": "",
    "delivery_terms": "Не определено",
    "potential_vol": "25",
    "kp_price": "10",
    "vol": "13",
    "price": "11223",
    "basis": "PE",
    "catalog": "RAL",
    "code": "2213",
    "shine": "ПОПО",
    "facture": "Гладкая",
    "temperature": "SSSSS",
    "postforming": 0,
    "applying": "НVZHUH",
    "surface_thin": "OMG",
    "surface_type": "ЖОПО",
    "comment": "POLOVOY HUY",
    "metallic": 1,
    "chameleon": 1,
    "antibacterial": 0,
    "antigraffiti": 0,
    "architect": 0,
    "zinc": 0
}
edit2 = {
    "api_key":"Hvdtygevzr52unsrabsr5q1gA#a",
    "request_from":"amo",
    "state":"edit",
    "lead_id":"6698355",
    "paints_leads_id":"43",
    "product_type":"paint",
    "name":"RAL2515-PE-н/о-гл",
    "product":"Краска",
    "delivery_date":"",
    "shine": "aasda",
    "delivery_terms":"Самовывоз - завод",
    "vol":"","price":"",
    "basis":"PE",
    "catalog":"RAL",
    "code":"2517",
    "facture":"Мокрая",
    "temperature":"КОКОКО",
    "applying":"Внутренее",
    "postforming":0,
    "surface_thin":"",
    "comment":"OLOLOLO",
    "metallic":0,"chameleon":0,"antibacterial":0,"antigraffiti":0,"architect":0,"zinc":0
}

search = {
    'api_key': 'Hvdtygevzr52unsrabsr5q1gA#a',
    'request_from': 'amo',
    'state': 'get_paint_info',
    'lead_id': 111,
    'paints_leads_id': 57,
    'query': 'RAL'
}
send_email_to_lab = {
    'state': 'send_lab', 'manager_mail': 'c29sb3ZpZXZAc3RhcmR1c3RwYWludHMucnU=', 'manager_mail_pass': 'MzNLZ3RzbDEx', 
    'old_id': '111', 'new_id': 564, 'id': ['3', '4', '5', '7', '8', '9'], 
    'data_manager': {'man_login': 'stardustpaintsamo@mail.ru', 'man_name': 'Дмитрий', 'man_last_name': '', 'man_phone_number': ''
    }
}
paint_info = {"api_key":"Hvdtygevzr52unsrabsr5q1gA#a","request_from":"amo","state":"get_paint_info","paint_id":"10"}
def send_request():
    a = requests.post(URL2, json=to_send_2)
    print(a)
    print(a.text)
    logging.debug(a.text)


if __name__ == "__main__":
    send_request()
