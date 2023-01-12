import {reactive} from "vue";

export const global_data = reactive({
    is_mobile: false,
    current_scenario: {},
    room_list: {},
    light_list: {},
    lock_list: {},
    sensor_list: {},
    switch_list: {}
})

export function isObjectEmpty(obj) {
    if (obj === null || obj === undefined)
        return true;

    for (let i in obj)
        return false;
    return true;
}