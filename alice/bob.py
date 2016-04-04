'''
    Bob part in alice's package
'''

import requests


def say_hello(name='Alice'):
    '''
        Bob say hello
    '''
    return 'Hello {}'.format(name)


def get_json():
    '''
        Get an online JSON
    '''
    url = 'http://echo.jsontest.com/key/value/one/two'
    return requests.get(url).json()
