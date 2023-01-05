# a = 10
# b = 4
# s = a > b
# print(s)
#
# if s:
#     print("a больше b")
# else:
#     print("a меньше или равно b")
# from test import a

# a = 'Слово "Python" '
# b = " i'm "
# s = ''' Слово
# "Python"
#  i'm  '''
# print(a, b, s)
# print(s)
#
# a1 = 'Слово\n "Python" '
# print(a1)
#
# print('Привет', '\n', 'Диана')


# a = 'Hello'
# b = 'Word'
#
# print(a+' ' +b ) #конкатенация
# s = a+ ' ' +b
# print(s)


# a = ''
# b = str()

# print(' Hi '* 3)
# print(('Hi' + ',') * 3)

# a = 'Hello'
# print(len(a))
#
# num = 123
# num_s = str(num)
# print(len(num_s))

#Напишите программу, которая запрашивает у пользователя его имя, а затем выводит строку
# «Привет, …», где вместо многоточия имя пользователя. А вторая строка выведет имя


# a = input('Введите  имя пользователя')
# print('Привет, +a ')
# print(a * 3)

# a 'Hello'
# print(a[0] , [-1], a[2])
# print(a[0:2], a[2:], a[3]) # [a:b] от a до b не включая b
# print(a[1:4:2]) # [a:b:x] от a до b с шагом x
# a_1 = '0123456789'
# print(a_1[2:7:2], a_1 [:: 3], a_1 [::-1]) # [::3] 0 + 3 - 3 + 3 -6 + 3
# print(a, a_1)


#Вычислить сумму цифр случайного трёхзначного числа
# import random
#
#
# r = random.randint(100, 999)
# print(r)
# r_s = str(r) # '888'
# r_1 = int(r_s[0])
# r_2 = int(r_s[1])
# r_3 = int(r_s[2])
#
# print(r_1+r_2+r_3)


# a = 'ПРИВЕТ'
# print(a.isupper(), a.islower())
# a_l = a.lower()
# print(a, a_l)
#
# s1 = 'привет'
# if s1.isupper():
#     print('Верхний регистр ')
# else:
#     print('Нижний регистр')

# a = '123'
# print(a.isdigit())
#
# b = 'Hello'
# print(b.isalpha())

# a = 'Over One'
# a2 = a.replace('One', '1')
# a3 = a.replace(' ', '')
# print(a)
# print(a2)
# print(a3)

# b = 'Hello'
# print(b.index('l'))


# a = 'Python'
# print('n' in a)


# дз

# a_1 = '0123456789'
# print(a_1[0:4])
# print(a_1[-2])
# print(a_1[0:5])
# print(a_1[:8])
# print(a_1[2:9:2])
# print(a_1[1:10:2])
# print(a_1[::-1])
# print(a_1[-1:-10:-2])
# print(a_1[0:10])
# print(len(a_1))


# Доп задача
#
# Дана строка, состоящая ровно из двух слов, разделенных пробелом.
# Переставьте эти слова местами. Результат запишите в строку и
# выведите получившуюся строку.


# Примечание: решить без использования функции split
#
# s = 'Привет пользователь'
# p = s.find(' ')
# print(s[p+1:]+s[p] +s[:p])

# s = 'Привет админ'
# b = s[ s.index(' ')+1:]+' '+s[: s.index(' ')]
# print(b)




































