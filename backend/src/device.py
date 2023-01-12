from flask import Blueprint, jsonify, request
from sqlalchemy.orm import sessionmaker
import json

from src.util import state
from src.db import db

device = Blueprint('device', __name__)


@device.route('/change_device_name', methods=['GET', 'POST'])
def change_device_name():
    db_session = sessionmaker(bind=db)()

    try:
        device_info = json.loads(request.get_data())
        device_id = device_info['device_id']
        device_name = device_info['device_name']

        db_session.execute(
            'update device set device_name = \'%s\' '
            'where device_id = %s'
            % (device_name, device_id)
        )
        db_session.commit()
    except:
        db_session.close()
        jsonify({'state': state['UPDATE_DEVICE_FAIL']})

    db_session.close()
    return jsonify({'state': state['SUCCESS']})


@device.route('/change_device_model', methods=['GET', 'POST'])
def change_device_model():
    db_session = sessionmaker(bind=db)()

    try:
        device_info = json.loads(request.get_data())
        device_id = device_info['device_id']
        device_model = device_info['device_model']

        db_session.execute(
            'update device set device_model = \'%s\' '
            'where device_id = %s'
            % (device_model, device_id)
        )
        db_session.commit()
    except:
        db_session.close()
        jsonify({'state': state['UPDATE_DEVICE_FAIL']})

    db_session.close()
    return jsonify({'state': state['SUCCESS']})


@device.route('/change_device_room', methods=['GET', 'POST'])
def change_device_room():
    db_session = sessionmaker(bind=db)()

    try:
        device_info = json.loads(request.get_data())
        device_id = device_info['device_id']
        room_id = device_info['room_id']

        db_session.execute(
            'update device set room_id = %s '
            'where device_id = %s'
            % (room_id, device_id)
        )
        db_session.commit()
    except:
        db_session.close()
        jsonify({'state': state['UPDATE_DEVICE_FAIL']})

    db_session.close()
    return jsonify({'state': state['SUCCESS']})


@device.route('/change_device_icon', methods=['GET', 'POST'])
def change_device_icon():
    db_session = sessionmaker(bind=db)()

    try:
        device_info = json.loads(request.get_data())
        device_id = device_info['device_id']
        device_type = device_info['device_type']
        device_icon = device_info['device_icon']

        if device_type == 'light':
            db_session.execute(
                'update light set light_icon = %s '
                'where light_id = %s'
                % (device_icon, device_id)
            )
        elif device_type == 'lock':
            db_session.execute(
                'update `lock` set lock_icon = %s '
                'where lock_id = %s'
                % (device_icon, device_id)
            )
        elif device_type == 'sensor':
            db_session.execute(
                'update sensor set sensor_icon = %s '
                'where sensor_id = %s'
                % (device_icon, device_id)
            )
        elif device_type == 'switch':
            db_session.execute(
                'update `switch` set switch_icon = %s '
                'where switch_id = %s'
                % (device_icon, device_id)
            )

        db_session.commit()
    except:
        db_session.close()
        jsonify({'state': state['UPDATE_DEVICE_FAIL']})

    db_session.close()
    return jsonify({'state': state['SUCCESS']})


@device.route('delete_device', methods=['GET', 'POST'])
def delete_device():
    db_session = sessionmaker(bind=db)()
    try:
        device_data = json.loads(request.get_data())
        device_id = device_data['device_id']
        db_session.execute(
            'delete from device '
            'where device_id = \'%s\''
            % device_id
        )
        db_session.commit()
    except:
        db_session.close()
        return jsonify({'state': state['DELETE_DEVICE_FAIL']})

    db_session.close()
    return jsonify({'state': state['SUCCESS']})