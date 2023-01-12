from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import urandom

from src.user import user
from src.scenario import scenario
from src.room import room
from src.device import device
from src.light import light
from src.lock import lock
from src.sensor import sensor
from src.switch import switch

app = Flask(__name__)
app.secret_key = urandom(32)
CORS(app, supports_credentials=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:0322@localhost:3306/bs'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_ECHO'] = True

app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(scenario, url_prefix='/scenario')
app.register_blueprint(room, url_prefix='/room')
app.register_blueprint(device, url_prefix='/device')
app.register_blueprint(light, url_prefix='/light')
app.register_blueprint(lock, url_prefix='/lock')
app.register_blueprint(sensor, url_prefix='/sensor')
app.register_blueprint(switch, url_prefix='/switch')


if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')