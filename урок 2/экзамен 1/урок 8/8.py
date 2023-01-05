# Дан список list=[15,48,'hello',6,19,'world’].
# Все числа этого списка проверить на чётность. Если число чётное, то посчитать сумму его цифр. Если нечётное, то заменить  его на 1 в списке.
# Все слова: посчитать количество гласных и согласных.
# Вывести всё на экран
#
# list = [15,48, 'hello' , 6,19, 'world']
# s_num = 0
# gl_num = 0
# sogl_num = 0
# for i in list:
#     if type(i) is int:
#         if i % 2 == 0:
#             for z in str(i):
#                 s_num += int(z)
#             print(i,'Сумма цифр:' , s_num)
#             s_num = 0
#         else:
#             ind = list.index(i)
#             list[ind] = 1
#     elif type(i) is str:
#         for b in i:
#             if b in 'aeoiu':
#                 gl_num += 1
#             else:
#                 sogl_num += 1
# print('Количество глассных:' , gl_num)
# print('Количество соглассных:' , sogl_num)
# print(list)
#
# a = (1,2,3,4,5,6)
# b =(1,)
# print(a,b)
#
# a1 = 1,2,3,4,5,6
# print(a1 , type(a1))
#
# a2 = tuple() #пустой кортеж
# print(a2 , type(a2))
#
# a3 = () # пустой кортеж
# print(a3 , type(a3))

# a = (1,2,3,4,5,6)
# b = [1,2,3,4,5,6]
# print(a.__sizeof__())
# print(b.__sizeof__())

# a = (1,2, 'hi!' , 123, 4)
# b = list(a) # можно не добавлять новую переменную. a = list(a)
# b.append('hello')
# b_c = tuple(b)
# print(b_c)

# nested = (1, 'do',['param',10,20])
# a = nested[2]
# a.append(785)
# # nested[2].append(785)
# print(nested[2], type(nested[2]))
# print(nested)
# print(nested[2][0]) #распечатать param , индекс 0

# x = (1,2,3,4)
# y = (5,6,7,8)
# print(x + y )
# z = x * 2 # к спискам тоже можно применять
# print(z)
# z = x + y
# print(z)

# x = (1,2,2,3,4)
# print(x.count(2), len(x))
# print(x.index(4))


# x = (1,2,2,3,4)
# print('max:','max(x)', 'min:' , min(x)) # к спискам тоже можно применять

# x = ('python', 'java', 'c', 'js', 'aa')
# print('max:', max(x, key = len), 'min:', min(x, key = len)) # к спискам тоже можно применять

# x = (1,2,2,3,4)
# print(sum(x)) # к спискам тоже можжно применять

# a = (1,2, 'hi!' , 123, 4)
# if 'hi' in a:
#     print('hi')

# a = (1,2, 'hi!' , 123, 4)
# for i in a:
#     print(i)

# Задание 1
# Создайте кортеж из случайных 10 чисел.
# Найдите его максимальный минимальный

# import random
# a = [random.randint(0,100) for i in range(10)]
# a = tuple(a)
# print(a)
# print('max', max(a), 'min', min(a))


#Задание 2
# Заполните один кортеж десятью случайными числами от 0 до 5
# Также заполните второй кортеж числами от -5 до 0.
# Объедините два кортежа , создав тем самым третий кортеж.
# Выведите на экран третий кортеж и количество нулей в нем.

# import random
# a = tuple(random.randint(0,5) for i in range(10))
# b = tuple(random.randint(-5,0) for i  in range(10))
# x = a + b
# print(x, '\n Количество нулей:', x.count(0))


#Задание 3
# Вывести данные кортежа без скобок, через запятую.
# Примечание: используйте кортеж строк

# a = (1,3, 'hi', 123, 4)
# x = ','.join([str(i) for i in a])
# print(x)

# дз.
# 1.Найти самое длинное слово в строке
# 2.Преобразовать текст в кортеж слов с удалением знаков препинания.
#
# a = 'how are you?!!'
# b = ''
# arr = []
# for i in a:
#         if i.isalpha():
#                 b += i
#         elif b != '':
#                 arr.append(b)
#                 b = ''
# if b != '':
#    arr.append(b)
# print(''.join(arr))
#
# print('max:' , max(arr,key=len))

#


# text = input("Введите текст: ")
# alpha = []
# for i in text:  # перебираем каждый элемент
#     if i.isalpha() or i == " ":  # создаем новый список без знаков.
#         alpha.append(i)
# cort = tuple("".join(alpha).split())  # преобразовал в строку, после в список и в кортеж
# print(cort, '\n'  "Самое длинное слово: ", max(cort, key=len))





















