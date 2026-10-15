class PartCoefficients:
    def __init__(self):
        self.coefficients = {
            "Капот": 1.0,
            "Передняя дверь": 1.2,
            "Задняя дверь": 1.1,
            "Передний бампер": 1.0,
            "Задний бампер": 1.0,
            "Крыша": 1.1,
        }

    def get(self, part):
        return self.coefficients[part.strip().capitalize()]