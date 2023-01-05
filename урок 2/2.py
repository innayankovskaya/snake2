# import random
# r = random.randint(100, 999 )
# print(r)
#
# a = 7
# b = 2.4
# l = False
# s = "Hello"
#
# # 1 вариант
# a2 = str(a)
# print(a2 , type(a2))
# b2 = str(b)
# print(b2 , type(b2))
#
#
# # 2 вариант
# a = str(a)
# print(a , type(a))
# b = str(b)
# print(b , type(b))

# a = int(input ("Введите первое целое число: "))
# b = int(input ("Введите второе целое число: "))
# c = input("Введите строку: ")
# d = float(input("Введите дробное число: "))
# print (a + b + d )
# print(c)

# # 1 вариант
# print(5 != 2) #
#
# # 2 вариант
# a = 3 != 3
# print(a)

# a = 3
# if a > 0:
#     print("a больше 0")
#
# print(" я не отношусь к ператору if")

# if True:
#     print("Привет")

# необходимо написать программу ,
# которая требует у пользователя ввести целое число и проверяет четное оно или нет .

# a = int(input("Число: "))
# if a % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")

# ch = input("Куда мы сегодня пойдем? ")
# if ch == "парк" :
#     print("Ура! Мы идем в парк")
# elif ch == "дом:" :
#     print("Ура! Мы остаемся дома")
# elif ch == "бар" :
#     print("Ура! Мы идем в бар")
# elif ch == "театр" :
#     print("Ура! Мы идем в театр")
# else:
#     print("Такого выбора не существует")

# a = int(input("Введите номер пальца: "))
# if a == 1:
#     print("большой палец")
# if a == 2:
#     print("указательный палец")
# if a == 3:
#     print("средний палец")
# if a == 4:
#     print("безымянный палец")
# if a == 5:
#     print("мизинец")
# else:
#     print("нет соответствий")

# a = int(input("Введите a "))
# b = int(input("Введите b "))
# c = int(input("Введите c "))
# if a  == 0 and b == 0:  # если у нас стоит and все выражения должны быть True
#     print("a = 0 И b = 0")
# elif a == 7 or b == 10:
#     print("a = 7 ИЛИ b = 10")
# elif a == 1 and b == 1 or c == 100:
#     print("a = 1 И b = 1 И c = 100")
# else:
#     print("нет соответствий")
#
# print(not True) # False
# print(not False) # True
# print(not (5 == 5)) # False

 # a = int(input("Введите a "))
 # b = int(input("Введите b "))
 # c = int(input("Введите c "))

 # if a > b and a > c:
 #     print("a наибольшее")
 # elif b > a and b > c:
 #     print("b наибольшее")
 # elif c > a and c > b:
 #     print("c наибольшее")


# # Написать примитивный калькулятор. Пользователь должен ввести число , потом операцию (+-*/)
# # и потом еще одно число , после этого пользователь получает ответ. Числа могут быть дробными.
#
# print("Введите число a=")
# a = int(input())
#
# print("Введите число b=")
# b = int(input())
#
# print("Выберите операцию")
# print("1 - сложить a + b")
# print("2 - вычесть a - b")
# c = int(input())
#
# if c == 1:
#     print("Сумма a + b =", a + b)
#
# if c == 2:
#     print("Разность a - b =", a - b)
#
# print("Введите число a =")
# a = int(input())
# print("Введите число b=")
# b = int(input())
#
# print("Выберите операцию")
# print("1 - умножить a * b")
# print("2 - делить a / b")
# c = int(input())
#
# if c == 1:
#     print("Произведение a * b =", a * b)
#
# if c == 2:
#     print("Часное a / b =", a / b)
# c = int(input())


# Лотерея. Реализуйте свою игру лотереи с выбором числа или набора чисел

# import random
# print("Компьютер загадает число от 0 до 30. Попробуйте угадать!")
# print("*" * 10, "Угадай число ", "*" * 10)
# print("Компьютер загадает число от 0 до 10. Попробуйте угадать!")
# answer = 1
# score = 0
# i = 0
# while answer:
#     if answer == 0:
#         break
#
#     rand = random.randint(1, 10)
#     answer = int(input("Число загаданно. Попробуйте угадать: "))
#     if answer == rand :
#         score = score + 1
#         print("Ты угадал")
#     else:
#         print("Ты не угадал! Пробуй еще")
#         i = i +1
#     print("Всего отгаданно чисел: ", score , "из", i)
#     print("Ждем вас снова")
#     print("Для выхода нажмите enter")


# # калькулятор 2
#
# m = input("Знак действия(+, -, *, /):")
# a = int(input("a = "))
# b = float(input("b = "))
#
# if m == "+":
#     print(a + b)
# elif m == "-":
#     print(a - b)
# elif m == "*":
#     print(a * b)
# elif m == "/":
#     print(a / b)


# Лотерея 2
#
# import random
#
# a = input('Введите название лотереи , которую хотите проверить')
#
# if a == 'Суперлото'
#     d = int(input('Введите 4 чисел вашего билета: '))
#     k = random.randint(1000 , 9999)
#     if d == k
#         print('Ваш билет выиграл')
#     else:
#         print('Попробуйте в другой раз!')
#
# elif a == 'Ваше лото':
#     q = input('Введите ваш номер телефона: ')
#     w = int(input('Введите ваш игровой номер из смс: '))
#     l = random.randint(10, 999)
#     if w == l:
#         print('Ваш билет выиграл')
#     else:
#         print('Попробуйте в другой раз')



































































