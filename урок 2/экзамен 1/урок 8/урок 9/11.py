#
# try:
#     a = 100 / 0
# except ZeroDivisionError:
#     print('произошло деление на ноль')
#     a = 0
# print('результат:' , a)


# try:
#     a = 100 / '0'
# except Exception as a:
#     print(a)
#     a = 0
# print('результат:' , a)

# d = {'a': 1, 'b': 2, 'c': 3}
#
# try:
#     value = d['v']
# except KeyError:   # ключ
#     print('ключа не существует!')

# l = {'a': 1, 'b': 2, 'c': 3}
#
# try:
#     a = l[7]
# except IndexError: # индекс
#     print('такого индекса не существует!')


# l = {'a': 1, 'b': 2, 'c': 3}
#
# try:
#     a = l[7]
# except IndexError: # индекс
#     print('такого индекса не существует!')
# except KeyError:   # ключ
#     print('ключа не существует!')
# except:
#     print('произошла другая ошибка')


# d = {'a': 1, 'b': 2, 'c': 3}
#
# try:
#     value = d['v']
# except ('KeyError', 'IndexError'):
#     print('произошла ошибка IndexError или KeyError ')

# d = {'a': 1, 'b': 2, 'c': 3}
#
# try:
#     value = d['v']
# except ('KeyError', 'IndexError'):
#     print('произошла ошибка IndexError или KeyError ')
# finally:
#     print('Оператор finally выполнен!')
#
# d = {'a': 1, 'b': 2, 'c': 3}
#
# try:
#     value = d['a']
# except ('KeyError', 'IndexError'):
#     print('произошла ошибка IndexError или KeyError ')
#
# else:
#     print('Ошибок не произошло')
# finally:
#     print('Оператор finally выполнен!')


# Введите два числа с клавиатуры.#Поделите одно на другое.
# Обработайте ошибку деления на ноль, если ошибок нет,
# то результат деления возвести в квадрат. Также используйте оператор finally.

# a = int(input("Введите 1 число:"))
# b = int(input("Введите 2 число:"))
# try:
#
#     c = a / b
# except ZeroDivisionError:
#     print("Произошло деление на ноль")
#     c = 0
#     print(c)
# else:
#     print(c ** 2)
#
# finally:
#
#     print("Оператор finally выполнен")


# дз
# Задача №1
#
# Ввод с клавиатуры. Если строка введённая с клавиатуры – это числа, то поделить первое на второе.
# Обработать ошибку деления на ноль. Если второе число 0, то программа запрашивает ввод чисел заново.
# Также если были введены буквы, то обработать исключение.
# Примечание: используйте ValueError для обработки исключения на тип данных.

# try:
#     a = int(input('Введите первое значение'))
#     b = int(input('Введите второе знаение'))
#     d = int(a) / int(b)
#     print('Поделить первое значение на второе:', d)
#
# except ZeroDivisionError:
#     print('Произошло деление на ноль')
#     d = 0
#     a = input('Введите первое значение')
#     b = input('Введите второе значение')
#     d = int(a) / int(b)
#     print('Ошибок нет!')
# except ValueError:
#     print('Введен неправильный тип данных')
# finally:
#     print('Операор finally выполнен')


# while True:
#     a = input('Введите строку')
#     arr = a.split()
#     try:
#         result = int(arr[0])/int(arr[1])
#     except ValueError:
#         print('Поддерживаются только числа')
#     except ZeroDivisionError:
#         print('Делить на ноль нельзя')
#     else:
#         print(result)
#         break
