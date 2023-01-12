create database bs;

create table bs.user (
    user_id integer primary key auto_increment,
    user_name varchar(128) not null unique,
    password varchar(20) not null,
    phone varchar(11) not null unique
);

create table bs.scenario (
    scenario_id integer primary key auto_increment,
    scenario_name varchar(128) not null,
    user_id integer not null,
    is_current bool not null,
    background_picture integer default 0,
    foreign key (user_id) references bs.user(user_id) on delete cascade
);

create table bs.room (
    room_id integer primary key auto_increment,
    room_name varchar(128) not null,
    scenario_id integer not null,
    foreign key (scenario_id) references bs.scenario(scenario_id) on delete cascade
);

create table bs.device (
    device_id integer primary key auto_increment,
    device_name varchar(128) not null,
    device_model varchar(128),
    device_type integer unsigned not null,
    room_id integer not null,
    device_x float,
    device_y float,
    foreign key (room_id) references bs.room(room_id) on delete cascade
);

create table bs.light (
    light_id integer primary key,
    light_state bool default false,
    luminance integer default 0,
    light_icon integer default 0,
    foreign key (light_id) references bs.device(device_id) on delete cascade
);

create table bs.lock (
    lock_id integer not null,
    lock_state bool default false,
    lock_icon integer default 0,
    foreign key (lock_id) references bs.device(device_id) on delete cascade
);

create table bs.sensor (
    sensor_id integer not null,
    sensor_state bool default false,
    temperature integer,
    humidity integer,
    is_main bool default false,
    sensor_icon integer default 0,
    foreign key (sensor_id) references bs.device(device_id) on delete cascade
);

create table bs.switch (
    switch_id integer not null,
    switch_state bool default false,
    switch_icon integer default 0,
    foreign key (switch_id) references bs.device(device_id) on delete cascade
);