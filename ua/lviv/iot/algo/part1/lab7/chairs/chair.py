"""
Module for the Chair class.
"""

from abc import ABC, abstractmethod

from ua.lviv.iot.algo.part1.lab7.decorators.log_method_call import log_method_call


@abstractmethod
class Chair(ABC):
    """
    A base abstract class for all chairs.
    Attributes:
        max_weight (float): The maximum weight the chair can handle.
        material (str): The material the chair is made of.
    """

    def __init__(self, max_weight=None, material=None):
        self.max_weight = max_weight
        self.material = material
        self.favourite_owner_set = set()

    def __str__(self):
        return f"Chair: {self.max_weight}, {self.material}"

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        yield self

    @abstractmethod
    def adjust_position(self, *args, **kwargs):
        """
        Adjusts the position of the chair.
        :return: None
        """

    @log_method_call
    def get_attributes_by_type(self, data_type):
        """
        Gets the attributes of the chair by the specified type.
        :param data_type: The type of the attributes to get.
        :type data_type: type
        :return: A dictionary of the attributes of the chair by the specified type.
        :rtype: dict
        """

        return {key: value for key, value in self.__dict__.items() if isinstance(value, data_type)}
