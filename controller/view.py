from app import app

from flask import request

from tasks import proceed_request

@app.route('/input', methods=['POST'])
def get_sensor():
    proceed_request.delay(request.form)
    return 'Ok'
