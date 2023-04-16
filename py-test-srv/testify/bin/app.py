import requests
from requests.auth import HTTPBasicAuth
import testify

from const import *

def fun_call(url: str, fun, auth: HTTPBasicAuth = None):
    # Additional headers.
    headers = {'Content-Type': 'application/json' } 

    if auth is not None:
        return fun(url, headers=headers, auth=auth)
    else:
        return fun(url, headers=headers)
    
def get_equals(url: str, fun_ptr):
    
    resp = fun_call(url, fun_ptr, HTTPBasicAuth('user', 'pass'))

    return resp.json()

def assert_equal(url: str, fun_ptr):
    """assert that containts are equal"""
    after = get_equals(url, fun_ptr)
    testify.assert_equal(SMOKE, after)
    
    return 0

def assert_url(url: str, fun_ptr, code: int = 200, auth: HTTPBasicAuth = None):
    """assert that endpoint is valid"""
    
    resp = fun_call(url, fun_ptr, auth)

    testify.assert_equal(resp.status_code, code)

    return 0

class TestGet(testify.TestCase):
    """docstring for TestGet."""

    def test_auth_get_all_url(self):
        return assert_url(URL, requests.get, auth=HTTPBasicAuth('user', 'pass'))
    
    def test_unauth_get_all_url(self):
        return assert_url(URL, requests.get, code=401)
    
    def test_get_all_equal_output(self):
        return assert_equal(URL, requests.get)

if __name__ == '__main__':
    testify.run()
