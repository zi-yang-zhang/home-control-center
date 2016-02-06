from error.exceptions import *
ON = 'on'
OFF = 'off'
ACTIVE = 'active'
DE_ACTIVE = 'de_active'
CONTROLLER = 'controller'
POWER = 'power'
STATE = {
    ON: {'name': "ON", 'value': 0},
    OFF: {'name': "OFF", 'value': 1},
    ACTIVE: {'name': "ACTIVE", 'value': 2},
    DE_ACTIVE: {'name': "DE-ACTIVE", 'value': 3}

}

CONTROLLER_STATE = [STATE['active'], STATE['de_active']]
POWER_STATE = [STATE['on'], STATE['off']]
STATE_TYPE = {
    CONTROLLER: CONTROLLER_STATE,
    POWER: POWER_STATE
}


def type_check(state, state_type):
    if state_type not in STATE_TYPE:
        raise InvalidStateTypeError(state_type)
    if state not in STATE:
            raise InvalidStateError(state)
    if state_type is POWER and STATE.get(state) not in POWER_STATE:
        raise InvalidPowerStateError(state)
    if state_type is CONTROLLER and STATE.get(state) not in CONTROLLER_STATE:
        raise InvalidControllerStateError(state)


class ComponentState(object):
    def __init__(self, initial_power_state, initial_controller_state):
        type_check(initial_power_state, POWER)
        type_check(initial_controller_state, CONTROLLER)
        self._power_state = STATE.get(initial_power_state)
        self._controller_state = STATE.get(initial_controller_state)

    def get_controller_state_name(self):
        return repr(self._controller_state.get('name'))

    def get_controller_state(self):
            return self._controller_state

    def get_power_state_name(self):
        return repr(self._power_state.get('name'))

    def get_power_state(self):
            return self._power_state

    def toggle_state(self, state_type):
        if state_type is POWER:
            switch_to_index = 1 if POWER_STATE.index(self._power_state) == 0 else -1
            self._power_state = POWER_STATE[POWER_STATE.index(self._power_state) + switch_to_index]
        if state_type is CONTROLLER:
            switch_to_index = 1 if CONTROLLER_STATE.index(self._controller_state) == 0 else -1
            self._controller_state = CONTROLLER_STATE[CONTROLLER_STATE.index(self._controller_state) + switch_to_index]


class Component(object):

    def __init__(self, name, address, attributes, device_type):
        self._name = name
        self._address = address
        self._attributes = attributes
        self._device_type = device_type


