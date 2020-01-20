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
    print response.text
    print response.request.headers


def basic_oauth():
    headers = {'Authorization': 'token xxxxxxxxx'}
    # user/emails
    response = request.get(construct_url('user/emails'), headers=headers)
    print response.request.headers
    print response.text
    print response.status_code


from requests.auth import AuthBase


class GithubAuth(AuthBase):
    """docstring for GithubAuth"AuthBase def __init__(self, arg):
        super(GithubAuth,AuthBase.__init__()
        self.arg = arg
