from flask import Blueprint, jsonify, request
from sqlalchemy.orm import sessionmaker
import json

from src.util import state
from src.db import db

switch = Blueprint('switch', __name__)

@switch.route('/get_all_switches', methods=['GET', 'POST'])
def get_all_switches():
    db_session = sessionmaker(bind=db)()

    try:
        scenario_id = request.get_data().decode()
        switches = db_session.execute(
            'select `switch`.*, '
            '   device.device_name, device.device_model, device.device_x, device.device_y, '
            '   room.room_id, room.room_name, room.scenario_id '
            'from room, device, `switch` '
            'where room.scenario_id = %s and '
            '   room.room_id = device.room_id and '
            '   device.device_id = `switch`.switch_id'
            % (scenario_id)
        )

        switch_list = {}
        # [switch_id, switch_state, switch_icon,
        # device_name, device_model, device_x, device_y,
        # room_id, room_name, scenario_id]
        for switch in switches:
            switch_list[switch[0]] = {
                'switch_state': switch[1],
                'switch_icon':  switch[2],
                'device_name':  switch[3],
                'device_model': switch[4],
                'device_x':     switch[5],
                'device_y':     switch[6],
                'room_id':      switch[7],
                'room_name':    switch[8],
                'scenario_id':  switch[9]
            }
    except:
        db_session.close()
        return jsonify({'state': state['GET_DEVICE_FAIL']})

    db_session.close()
    return jsonify({
        'state': state['SUCCESS'],
        'switch_list': switch_list
    })


@switch.route('/change_switch_state', methods=['GET', 'POST'])
def change_switch_state():
    db_session = sessionmaker(bind=db)()

    try:
        switch_data = json.loads(request.get_data())
        switch_id = switch_data['switch_id']
        switch_state = switch_data['switch_state']

        db_session.execute(
            'update `switch` set `switch`.switch_state = %s '
            'where `switch`.switch_id = %s'
            % (not switch_state, switch_id)
        )
        db_session.commit()
    except:
        db_session.close()
        jsonify({'state': state['UPDATE_DEVICE_FAIL']})

    db_session.close()
    return jsonify({
        'state': state['SUCCESS'],
        'switch_state': not switch_state
    })


@switch.route('/change_switch_position', methods=['GET', 'POST'])
def change_sensor_position():
    db_session = sessionmaker(bind=db)()

    try:
        switch_data = json.loads(request.get_data().decode())
        for switch_id in switch_data:
            x = switch_data[switch_id]['device_x']
            y = switch_data[switch_id]['device_y']
            db_session.execute(
                'update device '
                'set device_x = %s, device_y = %s '
                'where device_id = %s'
                % (x, y, switch_id)
            )
            db_session.commit()
    except:
        db_session.close()
        return jsonify({'state': state['UPDATE_DEVICE_FAIL']})

    db_session.close()
    return jsonify({'state': state['SUCCESS']})


@switch.route('add_switch', methods=['GET', 'POST'])
def add_switch():
    db_session = sessionmaker(bind=db)()

    try:
        switch_data = json.loads(request.get_data())
        room_id = switch_data['room_id']
        db_session.execute(
            'insert into device(device_name, device_type ,room_id) '
            'values (\'开关\', 3, %s)'
            % room_id
        )
        res = db_session.execute(
            'select LAST_INSERT_ID()'
        )
        switch_id = res.first()[0]
        db_session.execute(
            'insert into `switch`(switch_id) '
            'values (%s)'
            % switch_id
        )

        db_session.commit()
        db_session.close()
        return jsonify({
            'state': state['SUCCESS'],
            'switch_id': switch_id
        })
    except:
        db_session.close()
        return jsonify({'state': state['ADD_DEVICE_FAIL']})