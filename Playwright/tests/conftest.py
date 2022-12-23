import pytest
import requests
from config import *
import datetime


@pytest.fixture()
def test_1_get_token():
    token = requests.post(url=url_token, json=params)
    return token.json()


@pytest.fixture()
def test_get_datetime():
    current_time = datetime.datetime.now()
    return current_time
