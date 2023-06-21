"""
Module that contains the GamingChair class.
"""

from abc import ABC

from ua.lviv.iot.algo.part1.lab7.chairs.chair import Chair


class GamingChair(Chair, ABC):
    """
    A class representing a gaming chair.

    Attributes:
        MIN_HEIGHT (float): The minimum height of the gaming chair.
        MAX_HEIGHT (float): The maximum height of the gaming chair.
        max_weight (float): The maximum weight the chair can handle.
        material (str): The material the chair is made of.
        height (float): The height of the gaming chair.
        has_footrest (bool): Whether the gaming chair has a footrest.
    """
    MIN_HEIGHT = 1.2
    MAX_HEIGHT = 1.8

    def __init__(self, max_weight, material, height, has_footrest):
        super().__init__(max_weight, material)
        self.height = height
        self.has_footrest = has_footrest
        self.favourite_owner_set = {"Oleksandr, Valerii"}

    def __str__(self):
        return f"GamingChair: " \
               f"{self.max_weight}, " \
               f"{self.material}, " \
               f"{self.height}, " \
               f"{self.has_footrest}"

    def __len__(self):
        return len(self.favourite_owner_set)

    def __str__(self):
        return f"GamingChair: {self.max_weight}, {self.material}, {self.height}, {self.has_footrest}"

    def adjust_position(self, delta_height):
        """
        Adjusts the height of the gaming chair.
        :arg delta_height: The amount of height to adjust the gaming chair by.
        :type delta_height: float
        :raises ValueError: If the height of the gaming chair is out of bounds.
        :return: The height of the gaming chair.
        """
        if self.MIN_HEIGHT <= self.height + delta_height <= self.MAX_HEIGHT:
            self.height += delta_height
        elif self.height + delta_height > self.MAX_HEIGHT:
            self.height = self.MAX_HEIGHT
        else:
            self.height = self.MIN_HEIGHT
        return self.height
