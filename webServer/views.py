import datetime
import json

from app import app, db

from flask import request, render_template, jsonify

from models import ManipulatorStatus


@app.route('/manipulator', methods=['POST'])
def set_status():
    form = request.form
    new_status = ManipulatorStatus(datetime=datetime.datetime.strptime(form['datetime'], '%Y-%m-%d %H:%M:%S.%f'),
                                status=form['status'])
    db.session.add(new_status)
    db.session.commit()

    return 'Ok'


@app.route('/', methods=['GET'])
def get_status():
    args = request.args
    data = args.get('data', None)
    if data:
        last_status = db.session.query(ManipulatorStatus).order_by(ManipulatorStatus.datetime.desc()).first()
        return jsonify({'status': last_status.status})
    else:
        return render_template('status.html')