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
    'request_form': 'amo',
    'state': 'get_lead_info',
    'lead_id': 131,

}

def send_request():
    a = requests.post(URL2, json=to_send_2)
    print(a)
    print(a.text)
    logging.debug(a.text)


if __name__ == "__main__":
    send_request()
