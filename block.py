class Block:
    def __init__(self, name, values):
        self.name = name
        self.values = values

    def __repr__(self):
        return f"{self.name}: " + " ".join([f"{v}" for v in self.values[:3]]) + " ..."
