class VisualGenerator:

    def __init__(self, name):
        self.name = name

    def modifyName(self, newName):
        self.name = newName

    def whoAmI(self):
        return self.name