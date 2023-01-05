# d = {}
# d = {'dict': 1, 'dictionary': 2}
# print(d)

# a = {'one': 1, 2: 'two', (3,4): [1,3,4,5]} #ключи - неизмен тип данных. тип значения все типы данных
# print(a)
#
# a = {'one': 1,
#      2: 'two',
#      (3, 4): [1, 3, 4, 5]}  # ключи - неизмен. тип данных; значения - все типы данных
# print(a)

# a = dict()
# a_2 = {}
# print(a, type(a), a_2, type(a_2))
#
# d = dict([(1, 'one'), ('one', [1, 2, 3]), (2, 2)])
# print(d)

# d = dict(one=1, two = 'hello') # ключи только строки
# print(d)

# d = dict.fromkeys(['a', 'b'])
# d_2 = dict.fromkeys(['a', 'b'], 100)
# print(d, '\n', d_2)
#
# import random
# d = {i: i**2 for i in range(7)}
# print(d)
#
# d_2 = {i: random.randint(1,10) for i in range(7)}
# print(d_2)
#
# key = ['a', 'b', 1, (2,3)]
# d_3 = {i: random.randint(1,10) for i in key}
# print(d_3)


# a = {'one': 1,
#      2: 'two',
#      (3, 4): [1, 3, 4, 5]}  # ключи - неизмен. тип данных; значения - все типы данных
# a[3] = 77 # добавлениие новой пары
# a[2] = 123 # изменение существующей пары
# print(a)
# print(a['one'])
# print(len(a))


# del #удалить элемент по ключу


# Операция in - определение наличия ключа в словаре
# Исходный словарь
# Salary = { 'Director': 120800.0,
#            'Secretary': 101150.25,
#            'Locksmith': 188200.00 }
# print(Salary)

# Удалить элемент по ключу 'Secretary' с проверкой
# key = 'Secretary'
# if key in Salary:
#     del Salary['Secretary']
#     print(Salary)

# Попытка удалить несуществующий ключ
# если ключа нету, то исключение KeyError не генерируется
# key2 = 5
# if key2 in Salary:
#     del Salary[key2]


#
# phone = {'pixel': [1, 2, 3, 4],
#          'samsung': ['a1', 'a2', 'a3', 'a4'],
#          'cost': {'pixel_3': 300, 'samsung_a1': 200}
#          }
# print(phone['pixel'][2])
# print(phone['cost']['pixel_3'])


# Операция not in - определение отсутствия ключа в словаре
# Формирование словаря слов с их числовым эквивалентом

# # 1. Сформировать пустой словарь
# Words = dict()  # Words = {}
#
# # 2. Ввести количество слов в словаре
# count = int(input("Количество слов в словаре: "))
#
# # 3. Цикл добавления слов
# i = 0
# while i < count:
#     print("Ввод слов")
#     wrd = input("Слово:")
#     value = int(input("Значение: "))
#
#     # Если ключа wrd нет в словаре, то добавить пару [wrd:value]
#     if wrd not in Words:
#         Words[wrd] = value
#     i = i + 1
# # Вывести сформированный словарь
# print(Words)


# функция zip . Сoздать словарь путем Объединения списков ключей и значений

# Numbers = dict(zip([1,2,3], ['One', 'Two', 'Three']))
# print(Numbers)


# month = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr'}
# for i in month:              #i -ключ
#     print(i,':', month[i])
#
# print(month.keys()) # возвращает только ключи
# print(month.values())   # возвращает только значения
# print(month.items())   # возвращает только список кортежей(вид)
#
# for key , values in month .items():  # для дз смотреть методы!
#     print(key, ':', values)

# Задание 1
# Создайте словарь person , в котором будут присутсвовать ключи name,age,city
# Выведите значение возраста из словаря person

# person = {'name': 'Inna', 'age': 27, 'city': 'Minsk'}
# print(person['age'])


# Задание 2
# Значениями словаря могут быть и списки.
# Создайте словарь с ключами BMW , Tesla и списками из 3-х моделей в качестве значений.
# Выведите первое и  последнее значения каждого из ключей.

# auto = {"BMW": [1, 2, 3],
#         "Tesla": ["s1", "s2", "s3"]
#         }
# print("1-я и 3-я модели BMW: ", auto["BMW"][0], auto["BMW"][2], "\n",  #[-1] последний индекс
#       "1-я и 3-я модели Tesla: ", auto["Tesla"][0], auto["Tesla"][2])

# Задание 3
# Исправьте ошибки в коде , чтобы получить требуемый вывод. (Вывод True)

# d1 = {'a':100. 'b':200. 'c': 300} # точки
# d2 = {a:300.b:200, d:400} # запятая , ковычки в а нужно, запятые
# print(d1['b']== d2['b'])
# True - т.к вывели и там и там значение 200.


# Задание 4
# Дан словарь с числовыми значениями. Необходимо их все перемножить и вывести на экран.

# a = {'a': 10, 'b': 2, 'c': 5}
# r = 1
# for i in a:      # i - отвечает за каждый ключ
#     r *= a[i]   # если найти сумму то просто ставим +
# print(r)

# ДЗ
# У вас есть словарь, где ключ – название продукта. Значение – список, который содержит
#  цену и кол-во товара.
# Выведите через ‘’–’’ название – цену – количество.
# С клавиатуры вводите название товара и его кол-во. n – выход из программы.
#  Посчитать цену выбранных товаров и сколько товаров осталось в изначальном списке.

#1 Вариант решения

# print('Список кодов товаров: яблоко-1, груша-2, виноград-3, бананы-4, мандарины-5, апельсины-6, кокос-7, киви-8')
# print('структура ассортимента: -название, -цена руб./кг, -наличие на складе, кг')
# Assort = {1: [5, 565],       # Ассортимент магазина
#           2: [7, 456],
#           3: [8, 317]}
# print('Ассортимент продуктов в наличии на данный момент: ')
# for i in Assort:
#     print('код товара:', i, '-', Assort[i][0], 'руб./кг' '-', Assort[i][1], end='; ')
# print()
# S = 0   # Стоимость покупки, руб
# while True:
#     N = input("Введите код продукта из списка кодов или 'n' для завершения: ")
#     if N == 'n':
#         break
#     elif int(N) in Assort:
#         M = int(input('введите вес продукта: '))
#         if M < int(Assort[int(N)][1]):
#             S += M * Assort[int(N)][0]
#             Assort[int(N)][1] = Assort[int(N)][1] - M
#         else:
#             print('Недостаточное количество продукта на складе')
#             continue
#     else:
#         print('Такого продукта нет, введите другой код')
#         continue
# print('Стоимость Вашей покупки, руб.: ', S)
# print('Оставшийся ассортимент на складе: ')
# for i in Assort:
#     print('код товара:', i, ';', 'цена, руб./кг:', Assort[i][0], ';', 'Количество на складе, кг:', Assort[i][1])
# print('Приходите к нам снова!')

# 2 вариант решения
#
# products = {'Apple': [4.5 , 10],
#             'Orange':[6.2 , 5],
#             'Pineapple':[10.0 , 1],
#             'Mango':[7.5 , 2],
#             'Banana':[3.8 , 10]}
# for key, value in products.items():
#     print(key, '-', value [], '-'[1])
#     cost = 0
# while True:
#     product = input('what?  (n - nothing)')
#     if product == 'n' or product not in products.keys():
#         break
#     qty = int(input('Haw many?'))
#     if qty > products[product][1]:
#         print('We dont have so  much.')
#         continue
#     cost += products[product][0] * qty
#     products[product][1] -= qty
# print('-', * 20)
# print('Price:', cost)
# print('-' * 20 )
# for key ,value in products.items():
#     print(key, '-', value[0], '-', value[1])





















# products = {"Рис": [1.2, 500], "Гречка": [1.4, 1000]}
# for key in products:
#     print(f"{key} - {products[key][0]} - {products[key][1]}")
# summ = 0
# name = ""
# while name != "n":
#     name = input("Введите название товара: ")
#     if name in products:
#         quantity = int(input("Введите количество: "))
#         products[name][1] = products[name][1] - quantity
#         summ += quantity * products[name][0]
#     elif name != "n":
#         print("Нет такого товара!")
#     if name == "n":
#         print("Покупка на сумму: ", round(summ, 2),'р.')
#         print("Остаток: ")
#         for key in products:
#             print(f"{key} - {products[key][1]}")





