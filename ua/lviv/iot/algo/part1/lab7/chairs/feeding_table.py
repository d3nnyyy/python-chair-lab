"""
Module for the FeedingTable class.
"""
from abc import ABC

from ua.lviv.iot.algo.part1.lab7.chairs.chair import Chair


class FeedingTable(Chair, ABC):
    """
    A class representing a feeding table chair.
    Attributes:
        MIN_HEIGHT (float): The minimum height of the feeding table.
        MAX_HEIGHT (float): The maximum height of the feeding table.
        max_weight (float): The maximum weight the chair can handle.
        material (str): The material the chair is made of.
        height (float): The height of the feeding table.
        child_age (int): The age of the child that will use the feeding table.
    """

    MIN_HEIGHT = 0.5
    MAX_HEIGHT = 1

    def __init__(self, max_weight, material, height, child_age):
        super().__init__(max_weight, material)
        self.height = height
        self.child_age = child_age
        self.favourite_owner_set = {"baby Max, baby Nadya"}

    def __str__(self):
        return f"FeedingTable: {self.max_weight}, {self.material}, {self.height}, {self.child_age}"

    def __len__(self):
        return len(self.favourite_owner_set)

    def adjust_position(self, delta_height):
        """
        Adjusts the height of the feeding table.
        :arg delta_height: The amount of height to adjust the feeding table by.
        :type delta_height: float
        :raises ValueError: If the height of the feeding table is out of bounds.
        :return: The height of the feeding table.
        """
        if self.MIN_HEIGHT <= self.height + delta_height <= self.MAX_HEIGHT:
            self.height += delta_height
        elif self.height + delta_height > self.MAX_HEIGHT:
            self.height = self.MAX_HEIGHT
        else:
            self.height = self.MIN_HEIGHT
        return self.height
