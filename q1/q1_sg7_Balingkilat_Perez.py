class Glassware:
    def __init__(self, material="Glass"):
        self.material = material


class Beaker(Glassware):
    def __init__(self, capacity_ml=250, material="Glass"):
        super().__init__(material)
        self.capacity_ml = capacity_ml


class Tray:
    def __init__(self):
        self.beakers = [Beaker() for _ in range(5)]