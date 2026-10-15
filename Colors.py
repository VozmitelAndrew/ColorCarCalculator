class ColorCoefficients:
    def __init__(self):
        self.coefficients = {
            "Белый": 1.0,
            "Синий": 1.0,
            "Желтый": 1.1,
            "Красный": 1.0,
            "Перламутровый": 1.2,
            "Серый металлик": 1.3,
        }

    def get(self, color):
        return self.coefficients[color]