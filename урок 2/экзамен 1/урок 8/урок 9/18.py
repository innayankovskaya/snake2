# def a_function():
#     '''функция которая просто печатает текст'''
#     print('You just created a function')
#
#
# a_function()

# for i in range(10):
#     a_function()
#
# def empty_function():
#     pass

# a = [1,2,3,4]
#
#
# def a_f():
#     print(a)
#
# a_f()


# Задание 1
# Создайте функцию , которая будет считать сумму чисел в списке.

# a = [3,5,8,9,14,25]
# def a_f():
#
# b = 0
# for i in a:
#     b += i
# print(b)
#
#
# a_f()

# или так
# import random
#
# b = [random.randint(10, 100) for i in range(10)]
#
#
# def b_f():
#     s = 0
#     for i in b:
#         s += i
#     print(s)
#
#
# b_f()

# Суммирует два числа
# def add (a,b):
#     return a + b
#
# print(add(1,2))

# def add(a, b):
#     return a + b
#
#
# print(add(1, 2))  # 3
# r = add(1, 2)
# print(r, type(r))
# print(add('Привет', ' Мир'))
# print(add([1, 2, 3], [4, 5, 6]))
# add(1, 2)


# def add(a, b=1):
#     print('a =', a, 'b =', b)
#     return a + b
#
#
# print(add(2))
# print(add(2, 5))
# print(add(b=2, a=5))

# def add(a=0, b=0):
#     print('a =', a, 'b =', b)
#     return a + b
#
# print(add())
# print(add(2))
# print(add(2, 5))
# print(add(b=2, a=5))
#
# def a_fun(*args, **kwargs):
#     print(args) # кортеж
#     for i in args:
#         print(i)
#     print(kwargs) # словарь
#     for k,v in kwargs.items():
#         print(k,v)
#
#
# a_fun(1,2,3, 'asd', n = 'asd', e = 12,fg = 3)
#
# def a_f():
#     global a # переменная а глобаль
#     a = 1
#     b = 2
#     return a + b
#
#
# def b_f():
#     c = 3
#     return a + c
#
# print(a_f())
# print(b_f())

# def fun1(a, b):
#     def fun2(x):
#         return x * x * x
#
#     return fun2(a) + fun2(b) # a = x = x **3 + b = x = x**3
#
#
# print(fun1(4, 5)) # 4**3 + 5**3  # 189

# def s(a,b): return a + b
#
# print(s(1,2))

# Задание 2
# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12),
# и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).
# Номер месяца вводить с клавиатуры.

# def season():
#     a = int(input("Введите число от 1 до 12: "))
#     if a == 12 or a == 1 or a == 2:
#         print("Зима")
#     elif a == 3 or a == 4 or a == 5:
#         print("Весна")
#     elif a == 6 or a == 7 or a == 8:
#         print("Лето")
#     else:
#         print("Осень")
#
#
# season()
# 2 вариант решения
# def get_season(a):
#     if a in range(1, 3):
#         print("Winter")
#     elif a in range(3, 6):
#         print("Spring")
#     elif a in range(6, 9):
#         print("Summer")
#     elif a in range(9, 12):
#         print("Autumn")
#     else:
#         print("Winter")
#
#     return a
#
#
# get_season(a)


# Задание 3
# Написать функцию square, принимающую 1 аргумент — сторону квадрата,
# и возвращающую 3 значения: периметр квадрата, площадь квадрата и диагональ квадрата.
# Сторону квадрата вводить с клавиатуры.

# a - сторона
# Периметр = 4 * a
# Площадь = 𝑎^2
# Диагональ = a√2
#
# a = int(input('введите длину стороны квадрата'))
# def square(a):
#     b = 4*a
#     print("периметр", b)
#     c = a * a
#     print("площадь", c)
#     d = a * (2 ** 0.5)
#     print("диагональ", d)
#     return b,c,d
# square(a)
# 2 вариант решения
# def get_quare(a):
#     return f"P={a * 4}, S={a  2}, D={a * 2  0.5}"
#
#
# print(get_quare(int(input())))


# дз.
# Простейший калькулятор c введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
# Обработать ошибку: “Деление на ноль”
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию).

def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def proisv(a, b):
    return a * b

#
# def delen(a, b):
#     try:
#         return f'result:, {a / b}'
#     except ZeroDivisionError:
#         return 'ZeroDivisionError!'
#
#
# while True:
#     print('two numbers:')
#     num1 = int(input('a='))
#     num2 = int(input('b='))
#     x = input('operator: + - * / 0-exit')
#     if x == '0':
#         break
#     if x == "+":
#         print('result:', plus(num1, num2))
#     elif x == "-":
#         print('result:', minus(num1, num2))
#     elif x == "*":
#         print('result:', proisv(num1, num2))
#     elif x == "/":
#         print('result:', delen(num1, num2))



