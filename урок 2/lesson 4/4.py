# for i in range(10):  # range(10) - 0 1 2 3 4 5 6 7 8 9
#     print('Hello')

# for i in range(10):# range(10) - 0 1 2 3 4 5 6 7 8 9
#     print(i)
#     if i == 5:
#         print('i = 5!!!!')

# for i in range(5, 10):# range(5,10) -  5 6 7 8 9
#      print(i)
#
# for i in range(1, 20,2):  # range(a,b,c) - диапазон от  до b не включая b с шагом c
#     print(i)

# for i in range(20, 1, -2):  # range(a,b,c) - диапазон от  до b не включая b с шагом c
#      print(i)

# for i in range(5, 10): # range(5,10) -  5 6 7 8 9 не включая 10
#       print(i , end = ' ')
#
# print()
# print('Я не отношусь к циклу for')

# for i in 'Я учу Python':
#     print(i)

# a = 'я учу PYTHON'
# a_new = ''
# for i in a:
#     # print(i)
#     if i.isupper():
#         # print(1, end = ' ')
#         print(a_new)
#         a_new = a_new + i #a_new += i
#
# print(a_new)

#
# a = input('Введите строку:')
# b = input('Введите символ:')
# a_new = ''
# for i in a:
#     # print(i)
#     if i != b:
#         # print(i, end=' ')
#         print(a_new)
#         a_new = a_new + i  # a_new += i
# print(a_new)

#Вводится начало, конец и шаг последовательности,
# нужно вывести на экран данную последовательность чисел.

# a = int(input('Введите начало:'))
# b = int(input('Введите конец:'))
# c = int(input('Введите шаг:'))
#
# for i in range(a, b, c):
#     print(i, end=' ')

# Вывести на экран все числа в диапазоне 54 до 156 кратные 5

# for i in range(54, 255, 5):
#     print(i)

# for i in range(55, 9184, 5):
#     print(i)
#
# a = [] # пустой список
#
# b = [12, 3, 456, 768, 234, 123, 654]
# s = ['hello', 'world' , 'array']
#
# for i in b:
#     print(i)
# for i in s:
#     print(i)
#
# print(len(b))
# print(len(s))

# b = [12, 3, 456, 768, 234, 123, 654]
# for i in b:
#     print(i)
#     if i == 768:
#         break
# print('Я не отношусь к циклу for')


# b = [12, 3, 456, 768, 234, 123, 654]
# for i in b:
#      if i == 768:
#          continue
#      print(i)
# print('Я не отношусь к циклу for')
#
# a = [2, 3, 6, 5, 1, 22, 4]
# b = []
# for i in a:
#     if i % 2 == 0:
#         print(i)
#         b.append(i)
# print(b)
# b.append(1234)
# print(b)


# a = [2, 5, 6, 2, 2]
# print(a.count(2))


# Массив чисел. Найти их сумму и произведение
# a = [2, 8, 10, 12]
# b = 0
# for i in a:
#     b+=i
#     print(b)

# a = [2, 8, 10, 12]
# p = 1
# for i in a:
#     p*=i
#     print(p)

# 1. Перемножить все нечетные значения в диапазоне от 1 до 100.

# a = [1,100,1]
# b = 1
# for i in range(1,100):
#     if i % 2!= 0:
#         b*=i
#         print(b)


# 2. Записать в массив все числа в диапазоне от 1 до 500 кратные 5

# a = [0,500,5]
# b = []
# for i in range(0, 500, 5):
#      print(i)
#      b.append(i)
# print(b)


# 3. Вывести на экран все четные значения в диапазоне от 1 до 497

# for i in range(0, 496 , 2):
#     print(i)

# 4. Дан массив чисел. Если число встречается более двух раз , то добавить его в новый массив.

# a = [1, 3, 1, 7, 4, 1, 8, 7, 6, 7 , 12 ]
# b =[]
# for i in a:
#     if a.count(i)>2:
#         print(i)
#         b.append(i)
# print(b)

# a = [1, 3, 6, 4, 32, 45, 4, 73, 42, 4, 23, 4]
# b = []
# for i in a:
#     if a.count(i)>=2 and i not in b:
#         # print(i)
#         b.append(i)






