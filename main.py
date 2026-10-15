from CarCalculator import CarCalculator

VERSION = "0.1.0"

if __name__ == "__main__":
    MyCalc = CarCalculator()
    part = input("Введите деталь: ")
    color = input("Введите цвет: ")
    price = MyCalc.calc(part, color)
    print(f"Стоимость покраски: {price} руб.")