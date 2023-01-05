# class Car:
#     def __str__(self):
#         return 'Объект класса Car'
#
#     def start(self):
#         print('Двигатель заведен')
#
#
# car_1 = Car()
# car_2 = Car()
# print(car_1)
# print(car_2)


# class Phone:
#
#     def init(self, color, model):
#         self.color = color
#         self.model = model
#
#     def check_sim(self, mobile_operator):
#         if mobile_operator == 'MTS':
#             print('Ваш оператор МТС', self.model)
#
#
# my_phone = Phone('Red', 'Pixel')
# my_phone.check_sim('MTS')
#
# class Phone:
#     def init(self, color, model):
#         self.color = color
#         self.model = model
#     def check_sim(self, mobile_operator):
#         if mobile_operator == 'MTS':
#             print('Ваш оператор МТС', self.model)
#     @staticmethod
#     def model_(model):
#         print('Model', model)
# my_phone = Phone('Red', 'Pixel')
# my_phone.check_sim('MTS')
# Phone.model_('i785')
# my_phone.model_('i213')


# class Phone:
#     def init(self, color, model):
#         self.color = color
#         self.model = model
#     def check_sim(self, mobile_operator):
#         if mobile_operator == 'MTS':
#             print('Ваш оператор МТС', self.model)
#     @staticmethod
#     def model_(model):
#         print('Model', model)

#     @classmethod
#     def toy_phone(cls, color):
#         toy_phone = cls(color, 'ToyPhone')
#         return toy_phone
# my_phone = Phone('Red', 'Pixel')
# my_phone.check_sim('MTS')
# Phone.model_('i785')
# my_phone.model_('i213')
# print(Phone.toy_phone('Red').model)


# Класс Human
# Создайте класс Human.
# Определите для него два статических поля: default_name и default_age.
# Создайте метод init(), который помимо self принимает еще два параметра:
# name и age. Для этих параметров задайте значения по умолчанию, используя свойства
# default_name и default_age.
# В методе init() определите четыре свойства:
# Публичные - name и age. Приватные - money и house.
# Реализуйте справочный метод info(), который будет выводить поля name, age, house и money.
# Реализуйте справочный статический метод default_info(), который будет выводить
# статические поля default_name и default_age.
# Реализуйте метод earn_money(), увеличивающий значение свойства money.

#
# class Human:
#     default_name = 'Inna'
#     default_age = 27
#
#     def __init__(self, name=default_name, age=default_age):
#         self.name = name
#         self.age = age
#         self.__money = 0
#         self.__house = None
#
#     def info(self):
#         print(self.name, self.age, self.__money, self.__house)
#
#     @staticmethod
#     def default_info():
#         print(Human.default_name, Human.default_age)
#
#     def earn_money(self, x):
#         self.__money += x
#         print(self.__money)
#
# human_obj = Human()
# human_obj.info()
# human_obj1 = Human('John', 32)
# human_obj1.info()
# human_obj1.earn_money(100)
# human_obj1.info()
# human_obj1.earn_money(100)
# human_obj1.info()


# Родительский класс
# class Phone:
#
#     # Инициализатор
#     def __init__(self):
#         self.is_on = False
#
#     # Включаем телефон
#     def turn_on(self):
#         self.is_on = True
#
#     # Если телефон включен, делаем звонок
#     def call(self):
#         if self.is_on:
#             print('Making call...')
# #
#
# # Унаследованный класс
# class MobilePhone(Phone):
#
#     # Добавляем новое свойство battery
#     def __init__(self):
#         super().__init__()
#         self.battery = 0
#
#     # Заряжаем телефон на величину переданного значения
#     def charge(self, num):
#         self.battery = num
#         print(f'Charging battery up to ... {self.battery}%')
#
#
# my_mobile_phone = MobilePhone()
# print(dir(my_mobile_phone))


# создаем класс Vehicle
# class Vehicle:
#
#     def vehicle_method(self):
#         print("Это родительский метод из класса Vehicle")
#
#
# # создаем класс Car, который наследует Vehicle
# class Car(Vehicle):
#
#     def car_method(self):
#         print("Это дочерний метод из класса Car")
#
#
# # создаем класс Cycle, который наследует Vehicle
# class Cycle(Vehicle):
#     def cycleMethod(self):
#         print("Это дочерний метод из класса Cycle")
#
#
# car_a = Car()
# car_a.vehicle_method()  # вызов метода родительского класса
# car_b = Cycle()
# car_b.vehicle_method()  # вызов метода родительского класса

#
# class Camera:
#     def camera_method(self):
#         print("Это родительский метод из класса Camera")
#
#     def info(self):
#         print('Camera')
#
#
# class Radio:
#     def radio_method(self):
#         print("Это родительский метод из класса Radio")
#
#     def info(self):
#         print('Radio')
#
#
# class CellPhone(Camera, Radio):
#     def cell_phone_method(self):
#         print("Это дочерний метод из класса CellPhone")
#
#
# cell_phone_a = CellPhone()
# cell_phone_a.camera_method()
# cell_phone_a.radio_method()
# cell_phone_a.info()


# Класс House
# 1. Создайте класс House
# 2. Создайте метод init() и определите внутри него два динамических свойства:
# _area и _price.
# 3. Свои начальные значения они получают из параметров метода init()
# 4. Создайте метод final_price(), который принимает в качестве параметра размер
# скидки и возвращает цену с учетом данной скидки.

# Класс House
# 1. Создайте класс House
# 2. Создайте метод __init__() и определите внутри него два динамических свойства: _area и _price.
# 3. Свои начальные значения они получают из параметров метода __init__()
# 4. Создайте метод final_price(), который принимает в качестве параметра размер скидки и возвращает цену с учетом данной скидки.
# class House:
#     def __init__(self, area, price):
#         self._area = area
#         self._price = price
#
#     def final_price(self, discount):
#         final_price = self._price * (100 - discount) / 100
#         print('Final price:', final_price)
#         return final_price


# Класс SmallHouse
# 1. Создайте класс SmallHouse, унаследовав его функционал от класса House
# 2. Внутри класса SmallHouse переопределите метод init() так, чтобы он создавал объект с площадью 40м2
#
# Класс SmallHouse
# 1. Создайте класс SmallHouse, унаследовав его функционал от класса House
# 2. Внутри класса SmallHouse переопределите метод __init__() так, чтобы он создавал объект с площадью 40м2
# class SmallHouse(House):
#     def __init__(self, price):
#         super().__init__(40, price)
#
#
# human_obj = Human()
# human_obj.info()
# human_obj1 = Human('John', 32)
# human_obj1.info()
# human_obj1.earn_money(100)
# human_obj1.info()
# human_obj1.earn_money(100)
# human_obj1.info()
# house1 = SmallHouse(400)
# human_obj1.buy_house(house1,50)
# human_obj1.info()


# Класс Human
#  1. Реализуйте приватный метод make_deal(), который будет отвечать за техническую
# реализацию покупки дома: уменьшать количество денег на счету и присваивать ссылку
# на только что купленный дом. В качестве аргументов данный метод принимает объект дома
# и его цену.
# 2.  Реализуйте метод buy_house(), который будет проверять, что у человека достаточно
# денег для покупки, и совершать сделку.
# Если денег слишком мало - нужно вывести предупреждение в консоль.
# Параметры метода: ссылка на дом и размер скидки
#
# class Human:
#     default_name = 'Irina'
#     default_age = 31
#
#     def __init__(self, name=default_name, age=default_age):
#         self.name = name
#         self.age = age
#         self.__money = 0
#         self.__house = None
#
#     def info(self):
#         print(self.name, self.age, self.__money, self.__house)
#
#     @staticmethod
#     def default_info():
#         print(Human.default_name, Human.default_age)
#
#     def earn_money(self, x):
#         self.__money += x
#         print(self.__money)
#
#     def __make_deal(self, house, price):
#         self.__money -= price
#         self.__house = house
#
#     def buy_house(self, house, discount):
#         price = house.final_price(discount)
#         if self.__money >= price:
#             self.__make_deal(house, price)
#             print('Купили дом')
#         else:
#             print('Нет денег(')


# # Родительский класс
# class Phone:
#
#     def __init__(self):
#         self.is_on = False
#
#     def turn_on(self):
#         pass
#
#     def call(self):
#         pass
#
#     # Метод, который выводит короткую сводку по классу Phone
#     def info(self):
#         print(f'Class name: {Phone.__name__}')
#         print(f'If phone is ON: {self.is_on}')
#
#
# # Унаследованный класс
# class MobilePhone(Phone):
#
#     def __init__(self):
#         super().__init__()
#         self.battery = 0
#     # Такой же метод, который выводит короткую сводку по классу MobilePhone
#     # Обратите внимание, что названия у методов совпадают - оба метода называются info()
#     # Однако их содержимое различается
#     def info(self):
#         print(f'Class name: {MobilePhone.__name__}')
#         print(f'If mobile phone is ON: {self.is_on}')
#         print(f'Battery level: {self.battery}')
#
# Демонстрационная функция
#
# Создаем список из классов
# В цикле перебираем список и для каждого элемента списка(а элемент - это класс)
# Создаем объект и вызываем метод info()
# Главная особенность: запись object.info() не дает информацию об объекте, для которого будет вызван метод info()
# Это может быть объект класса Phone, а может - объект класса MobilePhone
# И только в момент исполнения кода становится ясно, для какого именно объекта нужно вызывать метод info()
# def show_polymorphism():
#     for a in [Phone, MobilePhone]:
#         print('-------')
#         object = a()
#         object.info()
#
#
# show_polymorphism()


#ДЗ
# Класс Alphabet
# 1. Создайте класс Alphabet
# 2. Создайте метод __init__(), внутри которого будут определены два динамических свойства:
# 1) lang - язык и 2) letters - список букв. Начальные значения свойств берутся из входных параметров метода.
# 3. Создайте метод print(), который выведет в консоль буквы алфавита
# 4. Создайте метод letters_num(), который вернет количество букв в алфавите
#
# Класс EngAlphabet
# 1. Создайте класс EngAlphabet путем наследования от класса Alphabet
# 2. Создайте метод __init__(), внутри которого будет вызываться родительский метод __init__().
# В качестве параметров ему будут передаваться обозначение языка(например, 'En')
# и строка, состоящая из всех букв алфавита(можно воспользоваться свойством ascii_uppercase из модуля string).
# 3. Добавьте приватное статическое свойство __letters_num, которое будет хранить количество букв в алфавите.
# 4. Создайте метод is_en_letter(), который будет принимать букву в качестве параметра и определять,
# относится ли эта буква к английскому алфавиту.
# 5. Переопределите метод letters_num() - пусть в текущем классе классе он будет возвращать
# значение свойства __letters_num.
# 6. Создайте статический метод example(), который будет возвращать пример текста на английском языке.


#Тесты:
# 1. Создайте объект класса EngAlphabet
# 2. Напечатайте буквы алфавита для этого объекта
# 3. Выведите количество букв в алфавите
# 4. Проверьте, относится ли буква F к английскому алфавиту
# 5. Проверьте, относится ли буква Щ к английскому алфавиту
# 6. Выведите пример текста на английском языке
#
# class Alphabet:
#     def __init__(self, lang, letters):
#         self.lang = lang
#         self.letters = letters
#
#     def __str__(self):
#         print(str(self.letters))
#
#     def letter_1(self):
#         return len(self.letters)
#
# class EngAlphabet(Alphabet):
#
#     def __init__(self , lang , letters):
#         super().__init__(lang, letters)
#         self.__letters_1 = len(letters)
#
#     def is_en_letter(self,letter):
#         if letter in self.letters:
#             print('True')
#         else:
#             print('False')
#
#     def letter_1(self):
#         print(self.__letters_1)
#
#     @staticmethod
#     def example():
#         print('Hello user!')
#
#
# a = EngAlphabet('En', list(ascii_uppercase))
# print(a)





