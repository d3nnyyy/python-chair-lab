from abc import ABC, abstractmethod


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

    def __str__(self):
        return f"Chair: {self.max_weight}, {self.material}"

    @abstractmethod
    def adjust_position(self):
        """
        Abstract method to adjust the position of the chair.

        Raises:
            NotImplementedError: If the method is not implemented.

        Returns:
            None
        """
        pass
