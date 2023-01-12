from flask import Blueprint, jsonify, request
from sqlalchemy.orm import sessionmaker
import json

from src.util import state
from src.db import db

room = Blueprint('room', __name__)

@room.route('/change_room_name', methods=['GET', 'POST'])
def change_room_name():
    db_session = sessionmaker(bind=db)()

    try:
        room_data = json.loads(request.get_data())
        room_id = room_data['room_id']
        room_name = room_data['room_name']

        db_session.execute(
            'update room set room_name = \'%s\' '
            'where room_id = %s'
            % (room_name, room_id)
        )
        db_session.commit()
    except:
        db_session.close()
        return jsonify({'state': state['UPDATE_ROOM_FAIL']})

    db_session.close()
    return jsonify({'state': state['SUCCESS']})


@room.route('/get_all_rooms', methods=['GET', 'POST'])
def get_all_rooms():
    db_session = sessionmaker(bind=db)()

    try:
        scenario_data = json.loads(request.get_data())
        scenario_id = scenario_data['scenario_id']

        rooms = db_session.execute(
            'select room_id, room_name from room '
            'where scenario_id = %s'
            % scenario_id
        )
        db_session.close()

        room_list = {}
        for room in rooms:
            room_list[room[0]] = room[1]

        return jsonify({
            'state': state['SUCCESS'],
            'room_list': room_list
        })
    except:
        db_session.close()
        return jsonify({'state': state['UPDATE_ROOM_FAIL']})


@room.route('/add_room', methods=['GET', 'POST'])
def add_room():
    db_session = sessionmaker(bind=db)()

    try:
        room_data = json.loads(request.get_data())
        scenario_id = room_data['scenario_id']

        db_session.execute(
            'insert into room(room_name, scenario_id) '
            'values (\'房间\', %s)'
            % scenario_id
        )
        res = db_session.execute(
            'select LAST_INSERT_ID()'
        )
        room_id = res.first()[0]

        db_session.commit()
        db_session.close()
        return jsonify({
            'state': state['SUCCESS'],
            'room_id': room_id
        })
    except:
        db_session.close()
        return jsonify({'state': state['ADD_ROOM_FAIL']})


@room.route('/delete_room', methods=['GET', 'POST'])
def delete_room():
    db_session = sessionmaker(bind=db)()

    try:
        room_data = json.loads(request.get_data())
        room_id = room_data['room_id']
        db_session.execute(
            'delete from room '
            'where room_id = %s'
            % room_id
        )

        db_session.commit()
        db_session.close()
        return jsonify({'state': state['SUCCESS']})
    except:
        db_session.close()
        return jsonify({'state': state['DELETE_ROOM_FAIL']})