from abc import ABC

from ua.lviv.iot.algo.part1.lab7.chairs.chair import Chair


class OfficeChair(Chair, ABC):
    MIN_ANGLE = 90
    MAX_ANGLE = 135

    def __init__(self, max_weight, material, angle, has_wheels):
        super().__init__(max_weight, material)
        self.angle = angle
        self.has_wheels = has_wheels

    def __str__(self):
        return f"OfficeChair: {self.max_weight}, {self.material}, {self.angle}, {self.has_wheels}"

    def adjust_position(self, delta_angle):
        if self.MIN_ANGLE <= self.angle + delta_angle <= self.MAX_ANGLE:
            self.angle += delta_angle
        elif self.angle + delta_angle > self.MAX_ANGLE:
            self.angle = self.MAX_ANGLE
        else:
            self.angle = self.MIN_ANGLE
