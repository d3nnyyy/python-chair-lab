"""
This module contains exceptions for chairs package
"""


class InvalidHeightException(Exception):
    """
    Exception for invalid height
    """
    message = "Invalid height"

    def __init__(self):
        super().__init__(self.message)


class InvalidAngleException(Exception):
    """
    Exception for invalid angle
    """
    message = "Invalid angle"

    def __init__(self):
        super().__init__(self.message)
