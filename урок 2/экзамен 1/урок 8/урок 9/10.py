# a = {12, 42, 5, 5,5, 8, 9832} # повторения игнорирует.удаляет из множества
# print(a, type(a))
import random

# b = set()
# print(b, type(b))

# a_2 = {'Pythone', 'Java','JS'}
# print(a_2)
#
# a_3 ={1, 6, 'JS', 7, 2, 6}
# print(a_3)

# a_3 ={1, 6, 'JS', 7, 2, 6, (1,2,3)} #элементы множества- неизм. тип данных
# print(a_3)

# a = [2,3,4,5,'py','py',1,22,3,3]
# x = set(a)
# a_1 = list(x)
# print(set(a))
# print(a_1)

# months = {'Jan','Feb','March','Apr','June'}
# for m in months:
#     print(m)

# months = {'Jan','Feb','March','Apr','June'}
# print('Feb' in months)

# months = {'Jan','Feb','March','Apr','June'}
# months.add('Feb') # добавление элемента во множество.выводится на любом месте
# print(months)

# num_set = {1,2,3,4,5,6}
# num_set.discard(3) # удаление элемента
# print(num_set)

# num_set = {1,2,3,4,5,6}
# num_set.remove(3)
# print(num_set)

# num_set = {1,2,3,4,5,6}
# num_set.pop() # удаляет случайный элемент
# print(num_set)

# num_set = {1,2,3,4,5,6}
# num_set.clear() # удаляет все
# print(num_set)

# объединение множеств
# months_a = {'Jan','Feb','March','Apr','June'}
# months_b = {'Jule', 'Aug','Sept','Oct','Nov','Dec'}
# all_months = months_a.union(months_b)
# print(all_months)

# x = {1, 2, 3}
# y = {4, 5, 6}
# z = {7, 8, 9}
# output = x.union(y, z)
# output_2 = x | y | z
# print(output)
# print(output_2)

# Пересечение множеств
# x = {1, 2, 3}
# y = {4, 3, 6}
# print(x & y)

# разница множества
# A = {1, 2, 3}
# B = {4, 3, 6}
# print(A - B)
# print(B - A)

#  скопировать
# string_set = {'Nicholas', 'Michelle', 'Jonn' , 'Mercy'}
# x = string_set.copy()
# print(x)

# #является множество пересечением или нет
# names_a = {'Nicholas', 'Michelle', 'Jonn' , 'Mercy'}
# names_b = {'Jeff', 'Bosco', 'Teddy', 'Milly'}
# x = names_a.isdisjoint(names_b)
# print(x)

# names_a = {'Nicholas', 'Michelle', 'Jonn' , 'Mercy'}
# print(len(names_a))

# frozenset
# my_set = frozenset([1, 2, 3, -10, 40]) #неизмен.тип данных
# print(type(my_set))

# Задание 1
# Проверить, есть ли в последовательности чисел списка дубликаты.

# lst = [0, 0, 1, 2, 2, 3, 8, 9, 9]
# st = set(lst)
# print(len(st) == len(lst))

# Задание 2
# 1.Создать множество.
# 2.Создать неизменяемое множество.
# 3.Выполнить операцию объединения созданных множеств.
# 4.Выполнить операцию пересечения созданных множеств.

# a = {9, 6, 3}
# a_2 = frozenset([4, 2, 1])
# print(a | a_2)
# print(a & a_2)

# Задание 3
# Преобразовать текст в множество слов с удалением знаков препинания.
# Например: python, JS! C? преобразуется в python JS C

# a = 'python, JS! C?'
# for i in a:
#     if not i.isalpha() and i != ' ':
#         a = a.replace(i, '')
# print(a)
# b = a.split()
# print(b)
# b = set(b)
# print(b)


# Даны имена параллельных классов. Найти общие именна.
# Сколько учеников в каждом классе. В каком классе больше учеников?
#
# A = {'Irina', 'Alex', 'Edvard', 'Julia', 'Niki', 'Pit', 'Olga'}
# B = {'Grisha', "Petya", "Marta", "Irina", 'Megi'}
# print('Общее имя:', A & B)
# print('Кол-во учеников в "A" классе:', len(A))
# print('Кол-во учеников в "B" классе:', len(B))
#
# if len(A) > len(B):
#     print('В "A" классе больше учеников, чем в "B" классе ')
# else:
#     print('В "B" классе больше учеников, чем в "A" классе ')


# Даны 2 переменные со 100 рандомными цифрами в диапазоне от 1 до 999.
# Проверить через множество есть ли пересечения и вывеcти на экран.
# Найти количество повторяющихся чисел и вывести на экран

import random

# a = set([random.randint(1, 999) for i in range(100)])
# b = set([random.randint(1, 999) for i in range(100)])
# print(a, b)
# c = a & b
# print('пересечения:', c, 'повторяющихся чисел:', len(c))

# a = [random.randint(1, 999) for i in range(100)]
# b = [random.randint(1, 999) for i in range(100)]
# print(a)
# print(b)
# a = set(a)
# b = set(b)
# x = a.isdisjoint(b)
# print(x)
# z = (a & b)
# print(z, len(z))

#
# Случайным образом генерируется список из 1000 чисел в диапазоне от 10 до 100.
# Необходимо посчитать, сколько разных(неповторяющихся) чисел входит в этот список
# 1 вариант решения
# import random
# a = [random.randint(10, 100) for i in range(1000)]
# b = set([random.randint(10, 100) for i in range(1000)])
# print(len(b))

# 2 вариан решения
# list_1 = [random.randint(0, 5) for i in range(10)]
# print(list_1)
# r = 0
# for i in set(list_1):
#     # print(i)
#     if list_1.count(i) == 1:
#         print(i)
#         r += 1
# print('кол-во чисел: ', r)



# Дано множество целых чисел {-3, 8, 15, -5, 0, 7}.
# Выведите на экран произведение максимального и минимального элементов

# a = {-3, 8, 15, -5, 0, 7}
# print(min(a)* max(a))

