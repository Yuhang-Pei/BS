from flask import Blueprint, jsonify, request, session
from sqlalchemy.orm import sessionmaker
import json

from src.db import db
from src.models import User
from src.util import state

user = Blueprint('user', __name__)

@user.route('/verify', methods=['POST'])
def verify_session():
    return jsonify({'state': state['success']})


@user.route('/signup', methods=['POST'])
def sign_up():
    db_session = sessionmaker(bind=db)()

    sign_up_data = json.loads(request.get_data())
    user_name = sign_up_data['user_name']
    password = sign_up_data['password']
    phone = sign_up_data['phone']

    query_res = db_session.execute(
        'select * from user '
        'where user.phone = \'%s\''
        % phone
    )

    # check the existence of the phone number
    if query_res.first():
        print('reach')
        db_session.close()
        return jsonify({'state': state['USER_ALREADY_EXISTED']})

    db_session.execute(
        'insert into user(user_name, password, phone) '
        'values (\'%s\', \'%s\', \'%s\')'
        % (user_name, password, phone)
    )
    res = db_session.execute(
        'select LAST_INSERT_ID()'
    )
    user_id = res.first()[0]

    db_session.execute(
        'insert into scenario(scenario_name, user_id, is_current) '
        'values (\'我的家\', %s, true)'
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
        'user_id': user_id,
        'user_name': user_name,
        'phone': phone,
        'scenario_id': scenario_id
    })


@user.route('/login', methods=['GET', 'POST'])
def log_in():
    db_session = sessionmaker(bind=db)()

    log_in_data = json.loads(request.get_data())
    phone = log_in_data['phone']
    password = log_in_data['password']

    # check the existence of the phone number
    query_res = db_session.execute(
        'select * from user '
        'where user.phone = %s'
        % phone
    ).all()
    if not query_res:
        return jsonify({'state': state['USER_NOT_EXIST']})
    db_session.close()

    # check the correctness of the password
    if query_res[0].password != password:
        return jsonify({'state': state['WRONG_PASSWORD']})

    # save user_id into session
    session['user'] = query_res[0].user_id
    return jsonify({
        'state': state['SUCCESS'],
        'user_id': query_res[0].user_id,
        'user_name': query_res[0].user_name,
        'phone': query_res[0].phone
    })


@user.route('/logout',methods=['POST'])
def log_out():
    print('logout')
    try:
        session.pop('user')
    except:
        return jsonify({'state': state['ERROR']})
    else:
        return jsonify({'state': state['SUCCESS']})