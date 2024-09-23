class Figure:
    sides_count = 0
    def __init__(self, color = [], sides = [], filled = False):
        self. __sides = self.__is_valid_sides(sides)#В Python __is_validate_sides — это функция, которая проверяет, являются ли стороны треугольника сторонами другого треугольника с заданными координатами вершин.
        self. __color = self.__is_valid_color(color)#Это функция, которая проверяет, является ли строка допустимым цветом в формате RGB или RGBA. Функция принимает строку (например, «rgb(0, 0, 0)» или «rgba(0, 0, 0, 0.123456789)») и возвращает True, если формат правильный, или False в противном
        self.filled = filled
    def get_color(self):#Это определение метода get_color() в классе self. Метод возвращает цвет объекта.
        return self.__color
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
    def __is_valid_color(self, r, g, b):
        return all(isinstance(c, int) and 0 <= c <= 255 for c in [r, g, b])# функция all() возвращает True, если все элементы итерируемого объекта равны True, и False в противном случае
    def __is_valid_sides(self, sides):
        return all(isinstance(side, int) and side > 0 for side in sides) and len(sides) == self.sides_count
#Это функция на языке Python, которая проверяет правильность сторон многоугольника. Функция возвращает True, если все стороны являются целыми числами больше нуля и их количество равно количеству сторон многоугольника.
    def get_sides(self):
        return self.__sides
    def __len__(self):
        return  sum(self. get_sides())
    def set_sides(self, *sides):
        if self.__is_valid_sides(sides):
            self.__sides = list(sides)
class Circle(Figure):
    sides_count = 1
    def __init__ (self, color = [255], side1 = 0, filed = False):




