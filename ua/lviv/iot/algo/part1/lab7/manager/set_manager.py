"""
Module that contains the SetManager class.
"""


class SetManager:
    """
    Class that manages sets.
    """

    def __init__(self, regular_manager):
        """
        Initializes the SetManager class.
        :param regular_manager:
        """
        self.regular_manager = regular_manager

    def __iter__(self):
        """
        Iterates over the SetManager class.
        :return: None
        """
        for chair in self.regular_manager:
            yield from chair

    def __len__(self):
        """
        Gets the length of the SetManager class.
        :return: The length of the SetManager class.
        """
        return sum(len(chair) for chair in self.regular_manager)

    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError("Index out of range")

        for chair in self.regular_manager:
            if index < len(chair):
                return list(chair)[index]
            index -= len(chair)

        raise IndexError("Index out of range")
