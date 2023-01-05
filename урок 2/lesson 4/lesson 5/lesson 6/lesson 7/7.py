# a = ['hi', 'hello' , 'like' , 'python']
# for i in a:
#     if str (i).isalpha():
#         if type(i) is str:
#             print(i)
#             a.remove(i)
#             del a[a.index(i)]
#             a.pop(a.index(i))
# print(i)
import b as b

#метод split

# my_string = 'Apples', 'Oranges' , 'Pears', 'Bananas', 'Berries'
# a = my_string.split(' , ')
# print(a)

# my_string = 'Apples', 'Oranges' , 'Pears', 'Bananas', 'Berries'
# a = my_string.split(' , ' , 2)
# print(a)

#метод join

# my_arr = ['Apples', 'Oranges' , 'Pears', 'Bananas', 'Berries']
# a = ','.join(my_arr)
# print(a)

# print('привет' if 5==5 else 'пока') #редко используется такое написание

# Какой результат у этой программы???

# print('100 200 300 400'.count('0'))  # 8 нолей во всей строке
# print('100 200 300 400'.count('0' , 3, 7))  # 2 раза в 200
# print('100 200 300 400'.count('0' , 3)) # 6 раз от 200 и до конца строки


# с клавиатуры вводится текст , определить , сколько в нем гласных , а сколько согласных
#
# a = input('Введите слово')
# gl = 0
# sogl = 0
#
# for i in a:
#     if i.lower() in  'aeiou':
#         gl += 1
#     else:
#         sogl += 1
# print('Гласные', gl)
# print('Согласные', sogl)


# вводятся три разных числа. найти , какое из них является средним (больше одного ,но меньше другого)

# print('Введите три числа:')

# a = int(input())
# b = int(input())
# c = int(input())
# if b < a < c or c < a <b :
#     print('Среднее:', a )
# elif a < b < c or c < b < a:
#     print('Среднее:', b)
# else:
#     print('Среднее:', c)

# или
# a = int(input())
# b = int(input())
# c = int(input())
# arr = []
# arr.append(a)
# arr.append(b)
# arr.append(c)
# print(arr)
# arr.sort()
# print(arr)
# print('Среднее:', arr[1] )

# Список из 7 цифр. Если четных цифр в нем больше , чем нечетных , то найти сумму всех его цифр
# , если нечетных больше , то найти произведение  1 3 и 6 элемента.

# a = [1,2,3,4,5,6,7]
# ch = 0
# n_ch = 0
# s = 0
# for i in a:
#     if i % 2 == 0:
#         ch +=1
#     else:
#         n_ch += 1
# print('Четные' , ch , 'Нечетные' , n_ch )
# if ch > n_ch:
#     print('Сумма', s)
# else:
#     print('произведение 1 3 и 6 элемента' , a[0] * a[2] * a[5])

# если дан не список из 7 цифр и просто произвольное число 1234567
# то нужно преобразовать к строке!
#
# a = 1234567
# ch = 0
# n_ch = 0
# s = 0
# for i in str(a):
#     i = int(i)
#     if i % 2 == 0:
#         ch +=1
#     else:
#         n_ch += 1






# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

# a1 = input('Введите целое число')
# a_list = list(a1)
# a_list.reverse()
# a2 = ''.join(a_list)
# print('Обратное ему число:' , a2)

# a = int(input('Введите число:'))
# b - str(a)
# b = b[:: -1]
# b = int(b)
# print(b)


#Введите слово c клавиатуры, которое состоит из букв разных регистров.
# Нужно посчитать кол-во пар верхнего регистра.
# Парой считаются две рядом стоящие буквы верхнего регистра.
# Например, HeLLoO – одна пара LL.

# a = input('Введите слово:')
# up = ''
# p_h = 0
# for i in a:
#     if i.isupper():
#         up += 1
#         if len(up) % 2 == 0:
#         p_h += 1
#         print(up)
#     elif up != '' :
#         up = ''
#
# # print(up)
# print(p_h)

#Вводиться строка. Удалить из неё все пробелы.
# После этого определить, является ли она палиндромом(перевертышем),
# т.е. одинаково пишется, как сначала, так и с конца

# s = input()
# n_s = s.replace('','')
# if n_s == n_s[::-1]:
#     print('Палиндром')
# else:
#     print('Не палиндром')

# s = input()
# s = s.split()
# s = ''. join(s)
# print(s)
# if s == s[::-1]:
#     print('Палиндром')
# else:
#     print('Не палиндром')


# дз.Посчитать, сколько раз встречается цифра 1 в списке чисел, заполненных рандомно.
# Диапазон случайного числа [1000, 9999]
# Кол-во чисел: 10


# import random
#
# r = [random.randint(1000,9999) for i in range(10)]
# print(r)
# a = str(r)
# print(a.count('1'))




# Дан список list=[15,48,'hello',6,19,'world’].
# Все числа этого списка проверить на чётность. Если число чётное, то посчитать сумму его цифр.
# Если нечётное, то заменить  его на 1 в списке.
# Все слова: посчитать количество гласных и согласных.
# Вывести всё на экран.

# list = [15,45, 'hello' , 6,19, 'world']
# a = []
# for i in list:
#     print(i)
#     if type(i) is str:
#         print(i)
#         a.appennd(i)
#
# print(a)
# a = ''.join(a)
# gl = 0
# sogl = 0
# for i in a:
#     if i in 'aeioy':
#         gl += 1
#     else:
#         sogl += 1
# print('Гласные' , gl)
# print('Согласные' , sogl)


























