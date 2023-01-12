from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'

    def __init__(self, user_name, password, phone):
        self.user_name = user_name
        self.password = password
        self.phone = phone

    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(128), nullable=False, unique=True)


class Scenario(db.Model):
    __tablename__ = 'scenario'

    scenario_id = db.Column(db.Integer, primary_key=True)
    scenario_name = db.Column(db.String(128), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    is_current = db.Column(db.Boolean, nullable=False)
    background_picture = db.Column(db.Integer, default=0)

    rooms = db.relationship('Room', primaryjoin='Scenario.scenario_id == Room.scenario_id', backref='scenario')


class Room(db.Model):
    __tablename__ = 'room'

    room_id = db.Column(db.Integer, primary_key=True)
    room_name = db.Column(db.String(128), nullable=False)
    scenario_id = db.Column(db.Integer, db.ForeignKey('scenario.scenario_id'), nullable=False)

    devices = db.relationship('Device', primaryjoin='Room.room_id == Device.room_id', backref='room')


class Device(db.Model):
    __tablename__ = 'device'

    device_id = db.Column(db.Integer, primary_key=True)
    device_name = db.Column(db.String(128), nullable=False)
    device_model = db.Column(db.String(128))
    device_type = db.Column(db.Integer, nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('room.room_id'), nullable=False)
    device_x = db.Column(db.Float)
    device_y = db.Column(db.Float)


class Light(db.Model):
    __tablename__ = 'light'

    light_id = db.Column(db.Integer, db.ForeignKey('device.device_id'), primary_key=True)
    light_state = db.Column(db.Boolean, default=False)
    luminance = db.Column(db.Integer, default=0)
    light_icon = db.Column(db.Integer, default=0)

    device = db.relationship('Device', primaryjoin='Device.device_id == Light.light_id')


class Lock(db.Model):
    __tablename__ = 'lock'

    lock_id = db.Column(db.Integer, db.ForeignKey('device.device_id'), primary_key=True)
    lock_state = db.Column(db.Boolean, default=False)
    lock_icon = db.Column(db.Integer, default=0)

    device = db.relationship('Device', primaryjoin='Device.device_id == Lock.lock_id')


class Sensor(db.Model):
    __tablename__ = 'sensor'

    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.sensor_id'), primary_key=True)
    sensor_state = db.Column(db.Boolean, default=False)
    temperature = db.Column(db.Integer)
    humidity = db.Column(db.Integer)
    is_main = db.Column(db.Boolean, default=False)
    sensor_icon = db.Column(db.Integer, default=0)

    device = db.relationship('Device', primaryjoin='Device.device_id == Sensor.sensor_id')


class Switch(db.Model):
    __tablename__ = 'switch'

    switch_id = db.Column(db.Integer, db.ForeignKey('device.device_id'), primary_key=True)
    switch_state = db.Column(db.Boolean, default=False)
    switch_icon = db.Column(db.Integer, default=0)

    device = db.relationship('Device', primaryjoin='Device.device_id == Switch.switch_id')