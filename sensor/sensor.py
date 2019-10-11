import datetime
import random
import socket

import requests

from utils import debounce

CONTROLLER_DOMAIN = 'controller:5000'

sensor_name = socket.gethostname()


@debounce(100)
def send_data(payload):
    data = {
        'datetime': datetime.datetime.now(),
        'payload': payload,
        'sensor': sensor_name
    }
    try:
        requests.post(f'http://{CONTROLLER_DOMAIN}/input', data=data)
    except:
        pass


if __name__ == '__main__':
    while True:
        send_data(random.randint(0, 5))


