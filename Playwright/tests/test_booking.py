import requests
from config import *
import pytest



def test_get_token():
    token = requests.post(url=url_token, json=params)
    print(token.json())
   
@pytest.mark.webtest
def test_update_booking(test_get_token):
    token = test_get_token
    print(token)
    r = requests.put(url=url_update, params=params_update)
    print(r.json())