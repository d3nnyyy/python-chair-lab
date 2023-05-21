class Chair:
    _instance = None

    def __init__(self):
        pass

    def __init__(self, max_weight=None, material=None, owner=None, id=1):
        self.max_weight = max_weight
        self.material = material
        self.owner = owner
        self.id = id

    def __str__(self):
        return f"Chair: {self.id}, {self.max_weight}, {self.material}, {self.owner}"


    @staticmethod
    def get_instance(max_weight=None, material=None, owner=None, id=1):
        if Chair._instance is None:
            Chair._instance = Chair(max_weight, material, owner, id)
        return Chair._instance

    def occupy(self, owner):
        self.owner = owner
        return f"Chair {self.id} is occupied by {self.owner}"

    def release(self):
        self.owner = None
        f"Chair {self.id} is released"

    def is_occupied(self):
        return self.owner is not None