from math import pi
import decimal


class Circle:
    def __init__(self, diameter: float):
        self._diameter: float = diameter
        self.__circle_long: decimal.Decimal = None
        self.__area: decimal.Decimal = None

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, diameter: float):
        self._diameter = diameter
        self.__circle_long = None
        self.__area = None

    @property
    def circle_long(self) -> decimal.Decimal:
        if self.__circle_long is None:
            self.__circle_long = decimal.Decimal(pi * self.diameter)
        return self.__circle_long

    @property
    def area(self) -> decimal.Decimal:
        if self.__area is None:
            self.__area = decimal.Decimal(pi * pow(self.diameter / 2, 2))
        return self.__area


# Пример использования класса Circle:
d = float(input("Введите диаметр круга: "))
circle = Circle(d)
print("Длина окружности:", circle.circle_long)
print("Площадь круга:", circle.area)


"""
1 Импортируются необходимые модули: math для значения pi и decimal для более точной работы с десятичными числами.
2 Определяется класс Circle, который представляет круг.
3 В конструкторе класса Circle задается инициализация объекта с помощью параметра diameter (диаметр круга).
4 Создаются приватные переменные __circle_long и __area с типом decimal.Decimal, которые будут использоваться для хранения вычисленных значений длины окружности и площади круга соответственно.
5 Определяется свойство diameter, которое позволяет получать и устанавливать значение диаметра круга. Внутри сеттера (метод с декоратором @diameter.setter) происходит обновление значения диаметра, а также сброс ранее вычисленных значений длины окружности и площади круга.
6 Определяется свойство circle_long, которое вычисляет и возвращает длину окружности круга. Если значение __circle_long еще не было вычислено (равно None), то оно вычисляется с использованием формулы pi * диаметр. Затем вычисленное значение возвращается.
7 Определяется свойство area, которое вычисляет и возвращает площадь круга. Если значение __area еще не было вычислено (равно None), то оно вычисляется с использованием формулы pi * (диаметр/2)^2. Затем вычисленное значение возвращается.
8 В последней части кода показан пример использования класса Circle. Пользователь вводит значение диаметра круга с помощью функции input, которое сохраняется в переменную d. Затем создается объект circle класса Circle с переданным в конструктор введенным значением диаметра.
9 Выводится длина окружности, полученная с помощью свойства circle_long, и площадь круга, полученная с помощью свойства area, на основе введенного значения диаметра.
"""

