from Colors import ColorCoefficients
from Parts import PartCoefficients


class CarCalculator:
    BASE_PRICE = 12000

    def __init__(self):
        self.colors = ColorCoefficients()
        self.parts = PartCoefficients()

    def calc(self, part, color):
        return self.BASE_PRICE * self.parts.get(part) * self.colors.get(color)