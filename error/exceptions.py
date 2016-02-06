class InvalidStateError(Exception):
    def __init__(self, state_name):
        self.state_name = state_name

    def __str__(self):
        return repr(self.state_name + " is not a valid state")


class InvalidPowerStateError(Exception):
    def __init__(self, state_name):
        self.state_name = state_name

    def __str__(self):
        return repr(self.state_name + " is not a valid power state")


class InvalidControllerStateError(Exception):
    def __init__(self, state_name):
        self.state_name = state_name

    def __str__(self):
        return repr(self.state_name + " is not a valid controller state")

class InvalidStateTypeError(Exception):
    def __init__(self, state_type):
        self.state_type = state_type

    def __str__(self):
        return repr(self.state_type + " is not a valid state type")
