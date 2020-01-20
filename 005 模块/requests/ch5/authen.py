# -*- coding: utf-8 -*-

import json
import requests

BASE_URL = 'https://api.github.com'


def construct_url(endpoint):
    return '/'.join([BASE_URL, endpoint])

def better_print(json_str):
    return json.dumps(json.loads(json_str), indent=4)

def basic_auth():
    """基本认证
    """
    response = requests.get(construct_url('user'), auth=('imoocdemo', 'imoocdemo123'))
    print better_print(response.text)
    print response.request.headers

basic_auth()
