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
