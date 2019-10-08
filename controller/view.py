from app import app

from flask import request

from tasks import proceed_request

@app.route('/input', methods=['POST'])
def hello_world():
    proceed_request.delay(request.form)
    print('request')

    return 'Hello World!'
