import datetime
import random

import requests

from utils import debounce

CONTROLLER_DOMAIN = 'controller:5000'

i = 0
@debounce(100)
def send_data(payload):
    global i
    data = {
        'datetime': datetime.datetime.now(),
        'payload': payload
    }
    try:
        requests.post(f'http://{CONTROLLER_DOMAIN}/input', data=data)
    except:
        pass


if __name__ == '__main__':
    while True:
        send_data(random.randint(0, 5))


