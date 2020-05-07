# -*- coding: utf-8 -*-

import requests
import base64
import logging


logging.basicConfig(level=logging.DEBUG, filename='log_test_request.txt', format='%(asctime)s %(levelname)s %(message)s')
URL = 'https://api.stardustpaints.ru/amoapi/send_email'
URL2 = 'https://api.stardustpaints.ru/amoapi/api/'

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
    "product": "Краска",
    "delivery_date": "",
    "delivery_terms": "Не определено",
    "potential_vol": "25",
    "kp_price": "10",
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
def send_request():
    a = requests.post(URL2, json=to_send_3)
    print(a)
    print(a.text)
    logging.debug(a.text)


if __name__ == "__main__":
    send_request()
