# elements = [1, 3, 'a' , 6 ,'b']
# print(elements)
#
# elements = list()
# print(elements)
#
# elements = [1, 3, 'a', 6, 'b']
# print(elements)
#
# print(elements[-1])
# print(elements[1:4])
# print(elements[::2])
# print(elements[:0:-3])



# import random
#
# a = [random.randint(100,999) for i in range(10)] # генерируем список из 10 чисел
# # (числа в диапазоне от 100 до 999)
# print(a,len(a))

# a = []
# a.append(1234)
# a.append('asdfghj')
# print(a)
# a.insert(0, 'Hello')
# print(a)
# a.insert(1, 789)
# print(a)


# elements = [1, 3, 'a', 6, 'b']
# elements[2] = 777
# print(elements)

# elements = [1, 3, 'a', 6, 'b']
# del elements[0] # удаляет 0 индекс т.е 1
# del elements[:: 2] # удаляет c шагом 2 и т.д
# del elements[1:5]
# print(elements)


# elements = [1, 3, 'a', 6, 'b']
# elements.remove('a')
# # elements.remove('a')
# print(elements)

# elements = [1, 3, 'a', 6, 'b']
# print('a' in elements)
#
# if 'a' in (elements):
#     print('Yes')

# a =[1, 2, 3 ]
# b = [4, 5, 6]
# # print(a+b) #канкатенация. объединили список
# # d = a+b
# # print(d)
# a.extend(b)
# print(a)

#
# elements = [1, 3, 'a', 6, 'b']
# for i in elements:
#     print(i)


# elements = [1, 3, 'a', 6, 'b', 'a']
# el_len = len(elements)
# i = 0
# while i < el_len:
#     print(elements[i])
#     i += 1


# a = [1,2,3]
# b = a # ссылка на объект а (так неправильно)
# a.append(123)
# b.append(134567)
# print(a,b)
# print(id(a), id(b))

# a = [1,2,3]
# b = a.copy()
# b.append(134567)
# print(id(a), id(b) , id(a) == id(b))


# a = [2, 3, 4, 5]
# x = a.pop(1) # удалить но не потерять навсегда . сохранить в переменную
# print(a ,x)

# a = [2, 3, 'Hello', 4, 5]
# i = a.index('Hello')
# # print(i)
# print(i , a[i])

# a = [2, 3, 'Hello', 4, 5]
# a.reverse()
# print(a)

import random

# a = [random.randint(1,10) for i in range(10)]
# print(a)
# a.sort() # по возрастанию
# print(a)
# a.sort(reverse = True) # на убывание
# print(a)

# a = ['w' , 'aww' , 'awca' , 'aa']
# a.sort(key=len) # по длинне строки. по умолчанию по алфавиту
# print(a)

# a = [2, 3, 'Hello',[4,5,6, 'H'] ,4, 5]
# a[3].append(45665879456)
# print(a)
# print(a[3] ,a[3][-2]) # предпоследний.т.е 'H'


# a = [ 9, 3, 14]
# a.reverse()
# print(a)

# a= [2,3,4,5]
# print(a)
# a.reverse()
# print(a)

#Дан список некоторых целых чисел, найдите значение 20 в нем и, если оно присутствует,
# замените его на 200. Обновите список только при первом вхождении числа 20.



# a = [1, 2, 3, 20, 1, 3]
# if 20 in a:
#     i = a.index(20)
#     a[i] = 200
# print(a)

# к дз.
# a = 'Hello'
# if type(a) is str:
#     print('Строка')


# Даны 2 списка:
# a = [4,6,'pу','tell',78]
# b = [44,'hello’,56,'exept’,3]
# Выполнить следующие операции:
# 1.Сложить два списка
# 2.Добавьте элемент 6 на 3 индекс.
# 3.Удалите все текстовые переменные
# 4.Посчитайте количество элементов списка

# 1
# a = [4,6,'pу','tell',78]
# b = [44, 'hello’,56, ', 3]
# print(a+b)

# 2.
# a = [4,6,'pу','tell',78]
# b = [44, 'hello' , 56 , 'exept' , 3]
# elements = [4,6,'pу','tell',78]
# elements.insert(3, 'tell 6')
# print(elements)

# elements = [44, 'hello' , 56 , 'exept' , 3]
# elements.insert(3, 'exept 6')
# print(elements)


# 3.
# elements = [4, 6, 'py' , 'tell' , 78]
# del elements[2]
# del elements[2]
# print(elements)

# elements = [44 , 'hello' , 56 , 'exept' , 3]
# elements.remove('hello')
# elements.remove('exept')
# print(elements)

# 4.
# a = [4,6,'pу','tell',78]
# print(len(a))
#
# b = [44, 'hello' , 56 , 'exept' , 3]
# print(len(b))











