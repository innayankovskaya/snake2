# class Car:
#     color = 'Grey'
#
#     def turn_on(self):
#         pass
#
#     def ride(self):
#         pass
#
#
# car_obj = Car()
# print(dir(Car))
#
# class Car:
#     # статические свойства
#     default_color = 'Grey'
#     default_weight = 5000
#     # динамические свойства
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model
#     def turn_on(self):
#         pass
#     def ride(self):
#         pass
#
#     def info(self):
#         return self.color, self.model, self.default_color, self.default_weight
# car_obj = Car('White', 'Model 1')
# car_obj2 = Car('Red', 'Model 2')
# # print(dir(Car))
# print(car_obj.default_color, car_obj.color)
# print(car_obj2.default_color, car_obj2.color)
# print(car_obj.info())

#Задача 1
#Напишите программу с классом Car.
# Создайте динамические свойства класса Car — color (цвет), type (тип), year (год).
# Напишите пять методов.
# Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен».
# Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен».
# Третий — присвоение автомобилю года выпуска.
# Четвертый метод — присвоение автомобилю типа.
# Пятый — присвоение автомобилю цвета
#
# class Car:
#     default_color = 'Black'
#     default_type = 'business'
#     default_year = 2015
#
#
#     def __init__(self, color, type, year):
#         self.color = color
#         self.type = type
#         self.year = year
#
#     def turn_on(self):
#         return 'Автомобиль заведен'
#     def turn_off(self):
#         return 'Автомобиль заглушен'
#     def year_made(self):
#         return self.year
#     def type_car(self):
#         return self.type
#     def color_type(self):
#         return self.color
#
#
# car_obj = Car('Black', 'business','2015')
# print(car_obj .turn_on())
# print(car_obj .turn_off())
# print(car_obj .year_made())
# print(car_obj .type_car())
# print(car_obj .color_type())

#или так
# class Car:
#     def __init__(self, year, type_car, color):
#         self.color = color
#         self.type_car = type_car
#         self.year = year
#
#     def func_z(self): print('Автомобиль заведен')
#
#     def func_vk(self): print('Автомобиль заглушен')
#
#     def func_year(self): print('Год машины', self.year)
#
#     def func_type(self): print(self.type_car)
#
#     def func_color(self): print(self.color)
#
#
# year = input('Введите год автомобиля ')
# type_car = input('Введите тип автомобиля ')
# color = input('Введите цвет автомобиля ')
# car = Car(year, type_car, color)
#
# car.func_z()
# car.func_vk()
# car.func_type()
# car.func_year()
# car.func_color()



#Задача 2
# Создайте класс Example. В нём пропишите 3 (метода) функции.
# Две переменные задайте статически, две динамически.
# Первая функция:создайте переменную внутри этой функции и выведите её
# Вторая функция:верните сумму 2-ух статичных переменных
# Третья функция:верните результат возведения первой динамической переменной во вторую
# динамическую переменную
# Создайте объект класса.
# Вызовите эти методы.
# Напечатайте первое статическое свойство.
#
# class Example:  # Класс
#     # Статические свойства
#     a = 4
#     b = 7
#     #динамические свойства
#
#     def __init__(self, d_1, d_2):
#         self.d_1 = d_1
#         self.d_2 = d_2
#
#     def func_1(self):
#         c = 5
#         print(c)
#
#     def func_2(self):
#         print(self.a + self.b)
#
#     def func_3(self):
#         print(self.d_1**self.d_2)
#
#
#
# E_obj = Example(4,2)  # создание объекта класса
#
# print(E_obj.func_1())
# print(E_obj.func_2())
# print(E_obj.func_3())

#или так
# class Example:
#     ex_a = 4
#     ex_b = 7
#
#     def __init__(self, d1, d2):
#         self.num1 = d1
#         self.num2 = d2
#
#     def func1(self):
#         v = 10
#         print(v)
#
#     def sum1(self):
#         return self.ex_a + self.ex_b
#
#     def degree(self):
#         return self.num1 ** self.num2
#
# example_obj = Example(2, 3)
# print(example_obj.sum1())
# print(example_obj.degree())
# example_obj.func1()


# дз

#Калькулятор.
# Создайте класс, где реализованы функции(методы) математических операций.
# А также функция, для ввод данных.

#
# class Calculator:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def summa(self): return a + b
#
#     def minus(self): return a - b
#
#     def umn(self): return a * b
#
#     def delenie(self): return a / b
#
#     def kvadrat(self): return a ** b
#
#     def procent(self): return a % b
#
# while True:
#
#     a = int(input('a = '))
#     b = int(input('b = '))
#     s = input('Введите + - * / % ** или "q" для выхода: ')
#
#     calculator_obj = Calculator(a, b)
#
#     if s == '-':
#         print(calculator_obj.minus())
#
#     elif s == '+':
#         print(calculator_obj.summa())
#
#     elif s == '/':
#         try:
#             print(calculator_obj.delenie())
#         except ZeroDivisionError:
#             print('На 0 делить нельзя!')
#
#     elif s == '*':
#         print(calculator_obj.umn())
#
#     elif s == '**':
#         print(calculator_obj.kvadrat())
#
#     elif s == '%':
#         print(calculator_obj.procent())
#
#     elif s == 'q':
#         break

