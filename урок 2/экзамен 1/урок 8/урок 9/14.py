# f = open('test.txt', 'r')
# print(f)
# print(*f)
# f.close()
import os

# f = open('test.txt', 'r', encoding='utf -8')
# print(f)
# print(*f)
# f.close()

# f = open('test.txt', 'r', encoding='utf -8')
# try:
#     print(*f)
# finally:
#     f.close()

# with open('test.txt', 'r', encoding='utf -8') as f:
#     print(*f)
# print('Не отношусь к блоку with')

# f = open('test.txt', 'r', encoding='utf -8')
# print(f.read(7))
# print(f.read(7))
# print(f.read)
# s = f.read()
# f.close()

# print(s, type(s))

# f = open('test.txt', 'r', encoding='utf -8')
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.close()

# f = open('test.txt', 'r', encoding='utf -8')
# print(f.readlines())
# f.close()

# f = open('test.txt', 'r', encoding='utf-8')
# # print(f.readline())
# # print(f.readline())
# # print(f.readline())
# # print(f.readlines())
# s = f.readlines()
# f.close()
#
# s_new = []
# for i in s:
#     i = i.replace('\n', '')  # rstrip()
#     s_new.append(i)
# print(s_new)


# f = open('123.txt', 'w', encoding='utf-8')#дополнительно найти режим на запись и чтение
# f.write('Hello \nWorld!') # на дозапись
# f.close()

# import os
# # os.rename('123', 'new_file.txt')
# print('Текущая директория:', os.getcwd())
#
# os.mkdir('folder')

# import os
#
# print('Текущая директория: ', os.getcwd())
# os.chdir('folder')
# print('Текущая директория: ', os.getcwd())
# f = open('123.txt', 'w', encoding='utf-8')
# f.write('Hello \nWorld!')
# f.close()

# import os
#
# print('Текущая директория: ', os.getcwd())
# os.chdir('folder')
# print('Текущая директория: ', os.getcwd())
# os.chdir('..')
# print('Текущая директория: ', os.getcwd())
# os.makedirs('n1/n2/n3')

# import os
# os.remove('folder/123.txt')

import os
# os.rmdir('folder')
# os.removedirs('n1/n2/n3')

#Задание 1
#В файле, в одну строку записаны слова и числа
# через пробел или _ найти сумму всех чисел.

# f = open('test.txt', 'r')
# s = f.read()
# f.close()
# print(s)
# s = s.replace(' ', '_')
# print(s)
# a = s.split('_')
# print(a)
# summ = 0
# for i in a:
#     if i.isdigit():
#         summ += int(i)
# print(summ)

# ДЗ
# Файл содержит числа и буквы. Каждый записан в отдельной строке.
# Нужно считать содержимое в список так, чтобы сначала шли числа по возрастанию,
# а потом слова по возрастанию их длинны.
#
# with open ('15.txt') as f:
#      s = f.readlines()
# print(s)
# b = []
# n =[]
# for i in s:
#     i = i.replace('\n', '')
#     if i.isalpha():
#         b.append(i)
#     elif i.isdigit():
#         n.append(int(i))
# print(b,n)
# n.sort()
# b.sort(key=len)
# mas = n + b
# print(mas)


# либо так
# with open("D_Z_14.txt", "r") as file:
#     lst = file.read().split()
#     lst_numbers = []
#     lst_words = []
#     for i in lst:
#         if i.isdigit():
#             lst_numbers.append(int(i))
#         else:
#             lst_words.append(i)
#     print(sorted(lst_numbers)+sorted(lst_words, key= len))

