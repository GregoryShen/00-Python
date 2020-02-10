import requests

BASE_URL = 'https://api.github.com'


def construct_url(end_ponit):
    return '/'.join([BASE_URL, end_ponit])


def basic_auth():
    """基本认证
    """
    response = requests.get(construct_url('user'), auth=('gregoryshentj@gmail.com', 'shenxin22019891'))
    print(response.text)
    print(response.request.headers)


def basic_oauth():
    headers = {'Authorization': 'token ff43fb7d15250964cf13d2d0ff4f8fd648ff3bb2'}
    response = requests.get(construct_url('user/emails'))
    print(response.request.headers)
    print(response.text)
    print(response.status_code)


# basic_oauth()

from requests.auth import AuthBase


class GithubAuth(AuthBase):

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        # request 加headers
        r.headers['Authorization'] = ' '.join(['token', self.token])
        return r


def oauth_advance():
    auth = GithubAuth('ff43fb7d15250964cf13d2d0ff4f8fd648ff3bb2')
    response = requests.get(construct_url('user/emails'), auth=auth)
    print(response.text)


oauth_advance()
