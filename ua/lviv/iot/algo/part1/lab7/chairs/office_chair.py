"""
Module that contains the OfficeChair class.
"""
from abc import ABC

from ua.lviv.iot.algo.part1.lab7.chairs.chair import Chair
from ua.lviv.iot.algo.part1.lab7.chairs.exceptions import InvalidAngleException
from ua.lviv.iot.algo.part1.lab7.decorators.log_exception import logged


class OfficeChair(Chair, ABC):
    """
    A class representing an office chair.
    Attributes:
        MIN_ANGLE (float): The minimum angle of the office chair.
        MAX_ANGLE (float): The maximum angle of the office chair.
        max_weight (float): The maximum weight the chair can handle.
        material (str): The material the chair is made of.
        angle (float): The angle of the office chair.
        has_wheels (bool): Whether the office chair has wheels.
    """
    MIN_ANGLE = 90
    MAX_ANGLE = 135

    def __init__(self, max_weight, material, angle, has_wheels):
        super().__init__(max_weight, material)
        self.angle = angle
        self.has_wheels = has_wheels
        self.favourite_owner_set = {"Mr Black, Mr Brown"}

    def __str__(self):
        return f"OfficeChair: {self.max_weight}, {self.material}, {self.angle}, {self.has_wheels}"

    def __len__(self):
        return len(self.favourite_owner_set)

    @logged(InvalidAngleException, "console")
    def adjust_position(self, delta_angle):
        """
        Adjusts the angle of the office chair.
        :param delta_angle: The amount of angle to adjust the office chair by.
        :type delta_angle: float
        :raises ValueError: If the angle of the office chair is out of bounds.
        :return: The angle of the office chair.
        """
        if not self.MIN_ANGLE <= self.angle + delta_angle <= self.MAX_ANGLE:
            raise InvalidAngleException
        self.angle += delta_angle
        return self.angle
