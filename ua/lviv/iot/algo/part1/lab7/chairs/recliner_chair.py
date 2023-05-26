from abc import ABC

from ua.lviv.iot.algo.part1.lab7.chairs.chair import Chair


class ReclinerChair(Chair, ABC):
    """
    A class representing a recliner chair.

    Attributes:
        MIN_ANGLE (float): The minimum angle of the recliner chair.
        MAX_ANGLE (float): The maximum angle of the recliner chair.
        max_weight (float): The maximum weight the chair can handle.
        material (str): The material the chair is made of.
        angle (float): The angle of the recliner chair.
        has_remote_control (bool): Whether the recliner chair has a remote control.
    """
    MIN_ANGLE = 90
    MAX_ANGLE = 150

    def __init__(self, max_weight, material, angle, has_remote_control):
        super().__init__(max_weight, material)
        self.angle = angle
        self.has_remote_control = has_remote_control

    def __str__(self):
        return f"ReclinerChair: {self.max_weight}, {self.material}, {self.angle}, {self.has_remote_control}"

    def adjust_position(self, delta_angle):
        """
        Adjusts the angle of the recliner chair.
        :param delta_angle: The amount of angle to adjust the recliner chair by.
        :type delta_angle: float
        :raises ValueError: If the angle of the recliner chair is out of bounds.
        """
        if self.MIN_ANGLE <= self.angle + delta_angle <= self.MAX_ANGLE:
            self.angle += delta_angle
        elif self.angle + delta_angle > self.MAX_ANGLE:
            self.angle = self.MAX_ANGLE
        else:
            self.angle = self.MIN_ANGLE
