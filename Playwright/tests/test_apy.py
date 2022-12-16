import requests
import pytest



def test_request_yandex():
    url = 'https://ya.ru'
    r = requests.get(url=url)
    assert r.status_code == 200