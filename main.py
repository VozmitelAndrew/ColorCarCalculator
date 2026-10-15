from CarCalculator import CarCalculator

VERSION = "0.2.0"

if __name__ == "__main__":
    MyCalc = CarCalculator()
    part = input("Введите деталь: ")
    color = input("Введите цвет: ")
    try:
        price = MyCalc.calc(part, color)
        print(f"Стоимость покраски: {price} руб.")
    except KeyError:
        print("Ошибка: такой детали или цвета нет в списке")