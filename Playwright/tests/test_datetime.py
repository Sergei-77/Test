import requests
import pytest
from config import *


def test_sen_req(test_get_datetime):
    r = "Current time is"
    time = test_get_datetime
    print(r, time)
