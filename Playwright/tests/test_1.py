import requests
import pytest

def test_request_status_code():
    url = 'https://reqres.in/api/users'
    params = 'page:2'
    r = requests.get(url=url, params=params)
    assert r.status_code == 200
    
def test_request_ya():
    url = 'https://ya.ru'
    r = requests.get(url=url)
    assert r.status_code == 200
    

    
    
