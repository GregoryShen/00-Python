# -*- coding: utf-8 -*-

import json
import requests
from requests import exceptions

URL = 'https://api.github.com'

def build_uri(endpoint):
    r = '/'.join([URL, endpoint])
    return r


def better_print(json_str):
    return json.dumps(json.loads(json_str), indent=4)


def request_method():
    #response = requests.get(build_uri('users/imoocdemo'))
    # print better_print(response.text)
    response = requests.get(build_uri('user/emails'), auth=('imoocdemo', 'imoocdemo123'))
    print better_print(response.text)

def params_request():
    response = requests.get(build_uri('users'), params={'since': 11})
    print better_print(response.text)
    print response.request.headers
    print response.url

def json_request():
    response = requests.patch(build_uri('user'), auth=('imoocdemo', 'imoocdemo123'), json={'name': 'babymooc2', 'email': 'hello-world@imooc.org'})
    print better_print(response.text)
    print response.request.headers
    print response.request.body
    print response.status_code

def timeout_request():
    try:
        response = requests.get(build_uri('user/emails'), timeout=10)
        response.raise_for_status()
    except exceptions.Timeout as e:
        print e.message
    except exceptions.HTTPError as e:
        print e.message
    else:
        print better_print(response.text)
        print response.status_code

def hard_requests():
    from requests import Request, Session
    s = Session()
    headers = {'User-Agent': 'fake1.3.4'}
    req = Request('GET', build_uri('users/emails'), auth=('imoocdemo', 'imoocdemo123'), headers=headers)
    prepared = req.prepare()
    print prepared.body
    print prepared.headers
    
    resp = s.send(prepared, timeout=5)
    print resp.status_code
    print resp.request.headers
    print better_print(resp.text)







if __name__ == '__main__':
    request_method()
    # build_uri('users/:GregoryShen')
    #params_request()
    # json_request()
    # timeout_request()
    # hard_requests()
