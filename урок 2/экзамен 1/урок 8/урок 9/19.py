# def factorial(n):
#     if n != 0:
#         return n * factorial(n -1)
#     else:
#         return 1
#
#
# print(factorial(5))

# def add(a, b):
#     return a + b
#
#
# variable = add(1,2)
#
# print(variable)

# def func(x): return x
#
#
# a1 = func
# a2 = a1
#
# print(a2(10))

# p = lambda x,y : x * y
# print(p(1,2)) # x = 1 y = 2

# p = lambda x =1,y =2 : x**y
# print(p())
# print(p(2,3))
# print(p(2))
# print(p(y=1,x=2))
# print(type(p))

# print((lambda x : x**2)(4))

# def func1(a):
#     def func2(b):
#         return a * b
#
#     return func2
#
#
# print(func1(2)(5)) # a = 2 b = 5
# t_func1 = func1(3)
# print(t_func1(5))
# print(t_func1(7))
# print(func1(1))
#
#
# def first_test():
#     print("Test function 1")
#
#
# def second_test():
#     print("Test function 2")
#
#
# def simple_decore(fn):
#     def wrapper():
#         print("Start function")
#         fn()
#         print("Stop function")
#
#     return wrapper
#
#
# first_test_wrapped = simple_decore(first_test)
# second_test_wrapped = simple_decore(second_test)
#
# first_test_wrapped()
# second_test_wrapped()

# def decor(fn):
#     def wrapper(arg):
#         print('Start function:', fn.__name__, 'with arg', arg )
#         fn(arg)
#     return wrapper
#
# @decor
# def print_sqrt(num):
#     print(num ** 0.5)
#
#
# print_sqrt(4) # 4= num = arg


#Задача 1
#Написать функцию , которая определяет количество разрядов введенного целого числа.

# def digits(n):
#     i = 0
#     while n > 0:
#         n = n // 10
#         i += 1
#     return i
#
#
# num = int(input('Введите число: '))
# print('Количество разрядов:', digits(num))

# или так

# def digits(n):
#     return len(str(n))
#
#
# num = int(input('Введите число: '))
# print('Количество разрядов:', digits(num))

#Задача 2
# Создайте функцию, которая принимает на вход неограниченное количество позиционных и
# именованных параметров, в качестве результата функция должна возвращать только
# позиционные параметры с нечетными индексами и ключевые,
# значения которых являются строками

# a = []
# b = []
#
#
# def fun(*args, **kwargs):
#     for i in args:
#         if args.index(i) % 2 != 0:
#             a.append(i)
#     for value in kwargs.values():
#         if type(value) is str:
#             b.append(value)
#     return a, b
#
#
# print(fun(1, 2, 3, 4, 5, name='Mike', job='programmer', num=123))

# Задача 3
# Написать функцию, которая заполняет массив длинной 10 элементов, случайными числами
# в диапазоне, указанном пользователем с клавиатуры.
# Функция должна принимать два аргумента – начало диапазона и его конец,
# при этом ничего не возвращать.

# import random
# def func(mn, mx):
#     arr = [random.randint(mn , mx) for i in range(10)]
#     print(arr)
#
# a = int(input('Начало диапазона:'))
# b = int(input('Конец диапазона'))
# func(a,b)

#Задача 4
# Создайте функцию, добавьте в неё локальное значение.
# Сделайте так, чтобы другая функция принимала это значение в качестве параметра.

# def fn():
#     a = 7
#     return a
#
# def fn_2(a):
#     return a
#
#
# print(fn_2(fn()))


# дз.
# Если в функцию передаётся кортеж, то посчитать длину всех его слов.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число – кол-во нечётных цифр.
# Строка – кол-во букв.
# Сделать проверку со всеми этими случаями.

# def f(x):
#
#     if type(x) is str:
#         print('количество букв' , len(x))
#     elif type(x) is list:
#         rek = []
#         vis = []
#         for i in str(x):
#             if i.isalpha():
#                 rek += 1
#             elif i.isdigit():
#                 vis += 1
#         print('количество букв', len(rek), ',', 'количество чисел', len(vis))
#     elif type(x) is tuple:
#         for i in x:
#             if type(i) is str:
#                 print('длина', x.index(i) +1, 'слов', len(i))
#             elif type(x) is int:
#                 j = str(x)
#                 a = 0
#                 for i in j:
#                     if int(i) % 2 !=0:
#                         a += 1
#                         print('нечетные цифры', j , '-', a)
#
#
# f('nike')
# f(['opyf'])
# f(('were', 'apple'))
# f(989)
#



# 2 вариант решения
# def check_input(a):
#     if type(a) is tuple:
#         print(*[len(i) for i in a])
#     elif type(a) is list:
#         print(sum([len(i) for i in "".join(a) if i.isdigit() or i.isalpha()]))
#     elif type(a) == float or type(a) == int:
#         print(len([i for i in str(a) if float(i) % 2 != 0]))
#     elif type(a) is str:
#         print(len([i for i in a if i.isalpha()]))
#
#
# check_input(("ad", "as", "dakjhkjh"))
# check_input(["ad", "as", "3[[[4443!3"])
# check_input(22777)
# check_input("6r66uttuu")














