from flask import Blueprint, jsonify, request, session
from sqlalchemy.orm import sessionmaker
import json
from PIL import Image
import io

from src.db import db
from src.models import Scenario, Room
from src.util import state, save_img

scenario = Blueprint('scenario', __name__)


@scenario.route('/get_scenario', methods=['GET', 'POST'])
def get_scenario():
    db_session = sessionmaker(bind=db)()

    try:
        scenario_data = json.loads(request.get_data())
        scenario_id = scenario_data['scenario_id']

        target = db_session.execute(
            'select scenario_name, is_current, background_picture '
            'from scenario '
            'where scenario_id = %s'
            % scenario_id
        ).first()

        return jsonify({
           'state': state['SUCCESS'],
            'scenario': {
                'scenario_name': target[0],
                'is_current': target[1],
                'background_picture': target[2]
            }
        })
    except:
        db_session.close()
        return jsonify({'state': state['GET_SCENARIO_FAIL']})


@scenario.route('/get_scenarios', methods=['GET', 'POST'])
def get_scenarios():
    db_session = sessionmaker(bind=db)()

    user_id = int(request.get_data())
    scenarios = db_session.execute(
        'select * '
        'from scenario '
        'where user_id = %s '
        % (user_id)
    )
    # scenarios = db_session.query(Scenario).filter(Scenario.user_id == user_id).all()
    scenario_list = {}
    current_scenario = -1
    for scenario in scenarios:
        # get the rooms in the scenario
        rooms = db_session.execute(
            'select * '
            'from room '
            'where room.scenario_id = %s '
            % (scenario.scenario_id)
        )
        room_list = {}
        for room in rooms:
            room_list[room.room_id] = room.room_name

        # add the info of the scenario into the list
        scenario_list[scenario.scenario_id] = {
            'scenario_name': scenario.scenario_name,
            'scenario_background': scenario.background_picture,
            'is_current': scenario.is_current,
            'room_list': room_list
        }

        # if this scenario is the current scenario, record it and jsonify it when returning
        if scenario.is_current:
            current_scenario = scenario.scenario_id

    return jsonify({
        'state': state['SUCCESS'],
        'current_scenario': current_scenario,
        'scenario_list': scenario_list
    })


@scenario.route('get_layout', methods=['GET', 'POST'])
def get_layout():
    try:
        db_session = sessionmaker(bind=db)()

        layout_data = json.loads(request.get_data())
        scenario_id = layout_data['scenario_id']

        layout_picture = db_session.execute(
            'select layout_picture '
            'from scenario '
            'where scenario_id = %s'
            % scenario_id
        ).first()[0]
        db_session.close()

        if not layout_picture:
            db_session.close()
            return jsonify({
                'state': state['SUCCESS'],
                'null': True
            })

        layout_path = '../data/img/' + layout_picture
        image = open(layout_path, 'rb').read()
        image = io.BytesIO(image)
        image = Image.open(image)

        image_byte_arr = io.BytesIO()
        image.save(image_byte_arr, format='PNG')
        image_byte_arr = image_byte_arr.getvalue()

        return image_byte_arr
    except:
        db_session.close()
        return jsonify({'state': state['GET_LAYOUT_FAIL']})


@scenario.route('/upload_layout', methods=['GET', 'POST'])
def upload_layout():
    try:
        db_session = sessionmaker(bind=db)()

        layout = request.files.get('file')
        user_id = request.values.get('user')
        scenario_id = request.values.get('scenario')
        layout_picture = str(user_id) + '.' + str(scenario_id) + '.jpg'
        layout_path = '../data/img/' + layout_picture
        layout.save(layout_path)

        db_session.execute(
            'update scenario '
            'set layout_picture = \'%s\' '
            'where scenario_id = %s'
            % (layout_picture, scenario_id)
        )

        db_session.commit()
    except:
        db_session.close()
        return jsonify({'state': state['UPLOAD_LAYOUT_FAIL']})

    db_session.close()
    return jsonify({
        'state': state['SUCCESS']
    });


@scenario.route('/change_scenario_name', methods=['GET', 'POST'])
def change_scenario_name():
    try:
        db_session = sessionmaker(bind=db)()

        scenario_data = json.loads(request.get_data())
        scenario_id = scenario_data['scenario_id']
        scenario_name = scenario_data['scenario_name']

        db_session.execute(
            'update scenario set scenario_name = \'%s\' '
            'where scenario_id = %s'
            % (scenario_name, scenario_id)
        )

        db_session.commit()
    except:
        db_session.close()
        return jsonify({'state': state['UPDATE_SCENARIO_FAIL']})

    db_session.close()
    return jsonify({
        'state': state['SUCCESS']
    })


@scenario.route('/change_background', methods=['GET', 'POST'])
def change_background():
    try:
        db_session = sessionmaker(bind=db)()

        scenario_data = json.loads(request.get_data())
        scenario_id = scenario_data['scenario_id']
        background = scenario_data['background']

        db_session.execute(
            'update scenario set background_picture = %s '
            'where scenario_id = %s'
            % (background, scenario_id)
        )

        db_session.commit()
    except:
        db_session.close()
        return jsonify({'state': state['UPDATE_SCENARIO_FAIL']})

    db_session.close()
    return jsonify({'state': state['SUCCESS']})


@scenario.route('/new_scenario', methods=['GET', 'POST'])
def new_scenario():
    try:
        db_session = sessionmaker(bind=db)()

        user_id = request.get_data().decode()
        print(user_id)
        db_session.execute(
            'insert into scenario(scenario_name, user_id, is_current) '
            'values (\'场景\', %s, false)'
            % user_id
        )
        res = db_session.execute(
            'select LAST_INSERT_ID()'
        )
        scenario_id = res.first()[0]

        db_session.commit()
        db_session.close()
        return jsonify({
            'state': state['SUCCESS'],
            'scenario_id': scenario_id
        })
    except:
        db_session.close()
        return jsonify({'state': state['UPDATE_SCENARIO_FAIL']})


@scenario.route('delete_scenario', methods=['GET', 'POST'])
def delete_scenario():
    db_session = sessionmaker(bind=db)()

    try:
        scenario_data = json.loads(request.get_data())
        scenario_id = scenario_data['scenario_id']
        db_session.execute(
            'delete from scenario '
            'where scenario_id = \'%s\''
            % scenario_id
        )
        db_session.commit()
    except:
        db_session.close()
        return jsonify({'state': state['DELETE_SCENARIO_FAIL']})

    db_session.close()
    return jsonify({'state': state['SUCCESS']})