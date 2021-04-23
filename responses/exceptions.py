class InvalidCommandException(Exception):
    pass


class InvalidArgumentException(Exception):
    pass


def invalid_command():
    raise InvalidCommandException("please enter a correct command")


def invalid_argument(string):
    raise InvalidArgumentException("please enter a correct " + string)
