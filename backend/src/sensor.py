from flask import Blueprint, jsonify, request
from sqlalchemy.orm import sessionmaker
import json

from src.util import state
from src.db import db
from simulation import simulate_sensor

sensor = Blueprint('sensor', __name__)


@sensor.route('/get_all_sensors', methods=['GET', 'POST'])
def get_all_sensors():
    db_session = sessionmaker(bind=db)()

    try:
        scenario_id = request.get_data().decode()
        sensors = db_session.execute(
            'select sensor.*, '
            '   device.device_name, device.device_model, device.device_x, device.device_y, '
            '   room.room_id, room.room_name, room.scenario_id '
            'from room, device, sensor '
            'where room.scenario_id = %s and '
            '   room.room_id = device.room_id and '
            '   device.device_id = sensor.sensor_id'
            % (scenario_id)
        )

        sensor_list = {}
        # [sensor_id, sensor_state, temperature, humidity, is_main, sensor_icon,
        # device_name, device_model, device_x, device_y,
        # room_id, room_name, scenario_id]
        for sensor in sensors:
            sensor_list[sensor[0]] = {
                'sensor_state': sensor[1],
                'temperature':  sensor[2],
                'humidity':     sensor[3],
                'is_main':      sensor[4],
                'sensor_icon':  sensor[5],
                'device_name':  sensor[6],
                'device_model': sensor[7],
                'device_x':     sensor[8],
                'device_y':     sensor[9],
                'room_id':      sensor[10],
                'room_name':    sensor[11],
                'scenario_id':  sensor[12]
            }
    except:
        db_session.close()
        return jsonify({'state': state['GET_DEVICE_FAIL']})

    db_session.close()
    return jsonify({
        'state': state['SUCCESS'],
        'sensor_list': sensor_list
    })


@sensor.route('/change_sensor_state', methods=['GET', 'POST'])
def change_sensor_state():
    db_session = sessionmaker(bind=db)()

    try:
        sensor_data = json.loads(request.get_data())
        sensor_id = sensor_data['sensor_id']
        sensor_state = sensor_data['sensor_state']

        # close the sensor
        if sensor_state:
            temperature = None
            humidity = None
            db_session.execute(
                'update sensor '
                'set sensor.sensor_state = false, '
                '   sensor.temperature = null, '
                '   sensor.humidity = null '
                'where sensor.sensor_id = %s'
                % sensor_id
            )
        else:
            temperature, humidity = simulate_sensor()
            db_session.execute(
                'update sensor '
                'set sensor.sensor_state = true, '
                '   sensor.temperature = %s, '
                '   sensor.humidity = %s ' 
                'where sensor.sensor_id = %s'
                % (temperature, humidity, sensor_id)
            )
        db_session.commit()
    except:
        db_session.close()
        jsonify({'state': state['UPDATE_DEVICE_FAIL']})

    db_session.close()
    return jsonify({
        'state': state['SUCCESS'],
        'sensor_state': not sensor_state,
        'temperature': temperature,
        'humidity': humidity
    })


@sensor.route('/change_main_sensor', methods=['GET', 'POST'])
def change_main_sensor():
    db_session = sessionmaker(bind=db)()

    try:
        sensor_data = json.loads(request.get_data())
        sensor_id = sensor_data['sensor_id']
        is_main = sensor_data['is_main']
        scenario_id = sensor_data['scenario_id']

        if is_main:
            db_session.execute(
                'update sensor set sensor.is_main = false '
                'where sensor.sensor_id = %s'
                % sensor_id
            )
            db_session.commit()
            db_session.close()
            return jsonify({
                'state': state['SUCCESS'],
                'current_main': None
            })
        else:
            db_session.execute(
                'update sensor set sensor.is_main = true '
                'where sensor.sensor_id = %s'
                % sensor_id
            )
            db_session.execute(
                'update sensor set sensor.is_main = false '
                'where sensor.sensor_id <> %s and '
                '   sensor.sensor_id in ('
                '       select device.device_id '
                '       from room, device '
                '       where room.scenario_id = %s and '
                '           room.room_id = device.room_id'
                ')'
                % (sensor_id, scenario_id)
            )
            db_session.commit()
            db_session.close()
            return jsonify({
                'state': state['SUCCESS'],
                'current_main_sensor': sensor_id
            })
    except:
        db_session.close()
        return jsonify({'state': state['UPDATE_DEVICE_FAIL']})


@sensor.route('/change_sensor_position', methods=['GET', 'POST'])
def change_sensor_position():
    db_session = sessionmaker(bind=db)()

    try:
        sensor_data = json.loads(request.get_data().decode())
        for sensor_id in sensor_data:
            x = sensor_data[sensor_id]['device_x']
            y = sensor_data[sensor_id]['device_y']
            db_session.execute(
                'update device '
                'set device_x = %s, device_y = %s '
                'where device_id = %s'
                % (x, y, sensor_id)
            )
            db_session.commit()
    except:
        db_session.close()
        return jsonify({'state': state['UPDATE_DEVICE_FAIL']})

    db_session.close()
    return jsonify({'state': state['SUCCESS']})


@sensor.route('add_sensor', methods=['GET', 'POST'])
def add_sensor():
    db_session = sessionmaker(bind=db)()

    try:
        sensor_data = json.loads(request.get_data())
        room_id = sensor_data['room_id']
        db_session.execute(
            'insert into device(device_name, device_type ,room_id) '
            'values (\'传感器\', 2, %s)'
            % room_id
        )
        res = db_session.execute(
            'select LAST_INSERT_ID()'
        )
        sensor_id = res.first()[0]
        db_session.execute(
            'insert into sensor(sensor_id) '
            'values (%s)'
            % sensor_id
        )

        db_session.commit()
        db_session.close()
        return jsonify({
            'state': state['SUCCESS'],
            'sensor_id': sensor_id
        })
    except:
        db_session.close()
        return jsonify({'state': state['ADD_DEVICE_FAIL']})