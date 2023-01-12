from flask import Blueprint, jsonify, request
from sqlalchemy.orm import sessionmaker
import json

from src.util import state
from src.db import db


lock = Blueprint('lock', __name__)


@lock.route('/get_all_locks', methods=['GET', 'POST'])
def get_all_locks():
    db_session = sessionmaker(bind=db)()

    try:
        scenario_id = request.get_data().decode()
        locks = db_session.execute(
            'select `lock`.*, '
            '   device.device_name, device.device_model, device.device_x, device.device_y, '
            '   room.room_id, room.room_name, room.scenario_id '
            'from room, device, `lock` '
            'where room.scenario_id = %s and '
            '   room.room_id = device.room_id and'
            '   device.device_id = `lock`.lock_id'
            % (scenario_id)
        )

        lock_list = {}
        # [lock_id, lock_state, lock_icon,
        # device_name, device_model, device_x, device_y,
        # room_id, room_name, scenario_id]
        for lock in locks:
            lock_list[lock[0]] = {
                'lock_state':   lock[1],
                'lock_icon':    lock[2],
                'device_name':  lock[3],
                'device_model': lock[4],
                'device_x':     lock[5],
                'device_y':     lock[6],
                'room_id':      lock[7],
                'room_name':    lock[8],
                'scenario_id':  lock[9]
            }

    except:
        db_session.close()
        return jsonify({'state': state['GET_DEVICE_FAIL']})

    db_session.close()
    return jsonify({
        'state': state['SUCCESS'],
        'lock_list': lock_list
    })


@lock.route('/change_lock_state', methods=['GET', 'POST'])
def change_lock_state():
    db_session = sessionmaker(bind=db)()

    try:
        lock_data = json.loads(request.get_data())
        lock_id = lock_data['lock_id']
        lock_state = lock_data['lock_state']

        db_session.execute(
            'update `lock` set `lock`.lock_state = %s '
            'where `lock`.lock_id = %s'
            % (not lock_state, lock_id)
        )
        db_session.commit()
    except:
        db_session.close()
        return jsonify({'state': state['UPDATE_DEVICE_FAIL']})

    db_session.close()
    return jsonify({
        'state': state['SUCCESS'],
        'lock_state': not lock_state
    })


@lock.route('/change_lock_position', methods=['GET', 'POST'])
def change_lock_position():
    db_session = sessionmaker(bind=db)()

    try:
        lock_data = json.loads(request.get_data().decode())
        for lock_id in lock_data:
            x = lock_data[lock_id]['device_x']
            y = lock_data[lock_id]['device_y']
            db_session.execute(
                'update device '
                'set device_x = %s, device_y = %s '
                'where device_id = %s'
                % (x, y, lock_id)
            )
            db_session.commit()
    except:
        db_session.close()
        return jsonify({'state': state['UPDATE_DEVICE_FAIL']})

    db_session.close()
    return jsonify({'state': state['SUCCESS']})


@lock.route('add_lock', methods=['GET', 'POST'])
def add_lock():
    db_session = sessionmaker(bind=db)()

    try:
        lock_data = json.loads(request.get_data())
        room_id = lock_data['room_id']
        db_session.execute(
            'insert into device(device_name, device_type ,room_id) '
            'values (\'锁\', 1, %s)'
            % room_id
        )
        res = db_session.execute(
            'select LAST_INSERT_ID()'
        )
        lock_id = res.first()[0]
        db_session.execute(
            'insert into `lock`(lock_id) '
            'values (%s)'
            % lock_id
        )

        db_session.commit()
        db_session.close()
        return jsonify({
            'state': state['SUCCESS'],
            'lock_id': lock_id
        })
    except:
        db_session.close()
        return jsonify({'state': state['ADD_DEVICE_FAIL']})