import requests
from config import *
import pytest


@pytest.fixture()
def test_get_token():
    token = requests.post(url=url_token, json=params)
    return token.json()