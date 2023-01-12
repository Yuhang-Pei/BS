from flask import session
import functools
import base64
import io


# 错误码
state = {
    'SUCCESS': 0,
    'ERROR': 1,
    'USER_ALREADY_EXISTED': 2,
    'USER_NOT_EXIST': 3,
    'WRONG_PASSWORD': 4,
    'ADD_SCENARIO_FAIL': 5,
    'DELETE_SCENARIO_FAIL': 6,
    'UPDATE_SCENARIO_FAIL': 7,
    'GET_SCENARIO_FAIL': 8,
    'ADD_ROOM_FAIL': 9,
    'DELETE_ROOM_FAIL': 10,
    'UPDATE_ROOM_FAIL': 11,
    'GET_ROOM_FAIL': 12,
    'ADD_DEVICE_FAIL': 13,
    'DELETE_DEVICE_FAIL': 14,
    'UPDATE_DEVICE_FAIL': 15,
    'GET_DEVICE_FAIL': 16,
    'UPLOAD_LAYOUT_FAIL': 17,
    'GET_LAYOUT_FAIL': 18,
    'LOGIN_REQUIRED': 19
}


device_type = {
    'LIGHT': 0,
    'LOCK': 1,
    'SENSOR': 2,
    'SWITCH': 3
}


# 修饰器，需要登录状态
def login_required(function):

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        print(session)
        if session.get('user'):
            return function(*args, **kwargs)
        else:
            return {"state": state["LOGIN_REQUIRED"]}

    return wrapper


# 图片操作
def save_img(pic, path):

    img = base64.b64decode(pic)
    img = io.BytesIO(img)
    print(img)
    # img = Image.open(img)

    # with open('tu.jpg', 'wb') as fp:
    #     fp.write(img)
    # image_data = np.fromstring(img, np.uint8)
    # print(image_data)