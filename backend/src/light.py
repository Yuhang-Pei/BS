from flask import Blueprint, jsonify, request
from sqlalchemy.orm import sessionmaker
import json

from src.util import state
from src.db import db
from interface import connect_light_int, change_light_state_int, change_light_luminance_int

light = Blueprint('light', __name__)


@light.route('/get_light', methods=['GET', 'POST'])
def get_light():
    db_session = sessionmaker(bind=db)()
    return jsonify({'state': state['SUCCESS']})


@light.route('/get_all_lights', methods=['GET', 'POST'])
def get_all_lights():
    db_session = sessionmaker(bind=db)()

    try:
        scenario_id = request.get_data().decode()
        lights = db_session.execute(
            'select light.*, '
            '   device.device_name, device.device_model, device.device_x, device.device_y, '
            '   room.room_id, room.room_name, room.scenario_id '
            'from room, device, light '
            'where room.scenario_id = %s and '
            '   room.room_id = device.room_id and '
            '   device.device_id = light.light_id'
            % (scenario_id)
        )

        light_list = {}
        # [light_id, light_state, luminance, light_icon,
        # device_name, device_model, device_x, device_y,
        # room_id, room_name, scenario_id]
        for light in lights:
            light_list[light[0]] = {
                'light_state':  light[1],
                'luminance':    light[2],
                'light_icon':   light[3],
                'device_name':  light[4],
                'device_model': light[5],
                'device_x':     light[6],
                'device_y':     light[7],
                'room_id':      light[8],
                'room_name':    light[9],
                'scenario_id':  light[10]
            }
    except:
        db_session.close()
        return jsonify({'state': state['GET_DEVICE_FAIL']})

    db_session.close()
    return jsonify({
        'state': state['SUCCESS'],
        'light_list': light_list
    })


@light.route('/change_light_state', methods=['GET', 'POST'])
def change_light_state():
    db_session = sessionmaker(bind=db)()

    try:
        light_data = json.loads(request.get_data())
        light_id = light_data['light_id']
        light_state = light_data['light_state']

        change_light_state_int()
        db_session.execute(
            'update light set light.light_state = %s '
            'where light.light_id = %s'
            % (not light_state, light_id)
        )
        db_session.commit()
    except:
        db_session.close()
        jsonify({'state': state['UPDATE_DEVICE_FAIL']})

    db_session.close()
    return jsonify({
        'state': state['SUCCESS'],
        'light_state': not light_state
    })


@light.route('/change_light_luminance', methods=['GET', 'POST'])
def change_light_luminance():
    db_session = sessionmaker(bind=db)()

    try:
        light_data = json.loads(request.get_data())
        light_id = light_data['light_id']
        luminance = light_data['luminance']

        change_light_luminance_int()
        db_session.execute(
            'update light set light.luminance = %s '
            'where light.light_id = %s'
            % (luminance, light_id)
        )
        db_session.commit()
    except:
        db_session.close()
        jsonify({'state': state['UPDATE_DEVICE_FAIL']})

    db_session.close()
    return jsonify({
        'state': state['SUCCESS'],
        'luminance': luminance
    })


@light.route('/change_light_position', methods=['GET', 'POST'])
def change_light_position():
    db_session = sessionmaker(bind=db)()

    try:
        light_data = json.loads(request.get_data().decode())
        for light_id in light_data:
            x = light_data[light_id]['device_x']
            y = light_data[light_id]['device_y']
            db_session.execute(
                'update device '
                'set device_x = %s, device_y = %s '
                'where device_id = %s'
                % (x, y, light_id)
            )
            db_session.commit()
    except:
        db_session.close()
        return jsonify({'state': state['UPDATE_DEVICE_FAIL']})

    db_session.close()
    return jsonify({'state': state['SUCCESS']})


@light.route('add_light', methods=['GET', 'POST'])
def add_light():
    db_session = sessionmaker(bind=db)()

    try:
        light_data = json.loads(request.get_data())
        room_id = light_data['room_id']
        connect_light_int()
        db_session.execute(
            'insert into device(device_name, device_type ,room_id) '
            'values (\'灯\', 0, %s)'
            % room_id
        )
        res = db_session.execute(
            'select LAST_INSERT_ID()'
        )
        light_id = res.first()[0]
        db_session.execute(
            'insert into light(light_id) '
            'values (%s)'
            % light_id
        )

        db_session.commit()
        db_session.close()
        return jsonify({
            'state': state['SUCCESS'],
            'light_id': light_id
        })
    except:
        db_session.close()
        return jsonify({'state': state['ADD_DEVICE_FAIL']})