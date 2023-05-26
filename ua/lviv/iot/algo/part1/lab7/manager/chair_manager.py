class ChairManager:
    """
    Class that manages chairs

    Attributes:
        chairs (list): A list of chairs.
    """
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
