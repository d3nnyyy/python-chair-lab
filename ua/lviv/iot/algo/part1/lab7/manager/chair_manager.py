"""
Module that contains the ChairManager class.
"""
from ua.lviv.iot.algo.part1.lab7.decorators.run_pylint import run_pylint


class ChairManager:
    """
    Class that manages chairs
    Attributes:
        chairs (list): A list of chairs.
    """

    def __len__(self):
        return len(self.chairs)

    def __getitem__(self, item):
        return self.chairs[item]

    def __iter__(self):
        return iter(self.chairs)

    chairs = []

    def find_chair_by_material(self, material):
        """
        Finds a chair by material.
        :param material: The material to find the chair by.
        :type material: str
        :return: A list of chairs with the specified material.
        :rtype: list
        """
        return [chair for chair in self.chairs if chair.material == material]

    def find_chair_with_max_weight_more_than(self, max_weight):
        """
        Finds a chair with a maximum weight more than the specified weight.
        :param max_weight: The maximum weight to find the chair by.
        :type max_weight: float
        :return: A list of chairs with a maximum weight more than the specified weight.
        :rtype: list
        """
        return [chair for chair in self.chairs if chair.max_weight > max_weight]

    def add_chair(self, chair):
        """
        Adds a chair to the list of chairs.
        :type chair: Chair
        :param chair: The chair to add.
        :return: None
        """
        self.chairs.append(chair)

    def get_results_of_adjust_position_functions(self):
        """
        Gets the results of the adjust_position functions of all chairs.
        :return: A list of the results of the adjust_position functions of all chairs.
        :rtype: list
        """

        return [chair.adjust_position(0.5) for chair in self.chairs]

    def enumerate_chairs(self):
        """
        Enumerates the chairs.
        :return: A list of enumerated chairs.
        :rtype: list
        """

        enumerated_chairs = list(enumerate(self.chairs))
        return enumerated_chairs

    def zip_object_and_results_of_adjust_position_functions(self):
        """
        Zips the chairs and the results of the adjust_position functions.
        :return: A list of zipped chairs and the results of the adjust_position functions.
        :rtype: list
        """
        zip_list = list(zip(self.chairs, self.get_results_of_adjust_position_functions()))
        return zip_list

    def get_chairs_dict(self):
        """
        Gets a dictionary of the chairs.
        :return: A dictionary of the chairs.
        :rtype: dict
        """
        return {index: str(chair) for index, chair in enumerate(self.chairs)}

    def if_any_chair_is_made_of_material(self, material):
        """
        Checks if any chair is made of the specified material.
        :param material: The material to check.
        :type material: str
        :return: True if any chair is made of the specified material, False otherwise.
        :rtype: bool
        """
        return any(chair.material == material for chair in self.chairs)

    def if_all_chairs_have_max_weight_more_than(self, weight):
        """
        Checks if all chairs have weight more than the specified weight.
        :param weight: The weight to check.
        :type weight: float
        :return: True if all chairs have weight more than the specified weight, False otherwise.
        :rtype: bool
        """
        return all(chair.max_weight > weight for chair in self.chairs)

    @run_pylint(__file__)
    def execute_pylint(self):
        """
        Runs pylint.
        :return: None
        """
        print("Pylint has been executed!!!")
