import datetime
import random

import requests

from sensor.utils import debounce

CONTROLLER_DOMAIN = 'sensor'

@debounce(100)
def send_data(payload):
    data = {
        'datetime': datetime.datetime.now(),
        'payload': payload
    }
    requests.post(f'http://{CONTROLLER_DOMAIN}/input', data=data)
    print(1)


if __name__ == '__main__':
    while True:
        send_data(random.randint())


