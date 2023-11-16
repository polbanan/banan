# class Item:
#     def __init__(self, name, price, weight):
#         self.name = name
#         self.price = price
#         self.weight = weight
#
#     def __add__(self, other):
#         if isinstance(other, Item):
#             return self.price + other.price
#         else:
#             return self.price + other
#
# item_1 = Item('МОнитор', 20_000, 5)
# item_2 = Item('Видюха', 15_000, 0.8)
# print(item_1.price + item_2.price)
# print(item_1.price - item_2.price)
# print(item_1.price * item_2.price)
# print(item_1.price / item_2.price)
# print(item_1 + item_2)
# print(item_1 + 10)

# from tkinter import *
# from random import randint
#
# window = Tk()
# window.geometry('600x600')
#
# canvas = Canvas(window, width=600, height=600)
# canvas.pack()
# class Fire:
#     image = PhotoImage(file='fire.png').subsample(4, 4)
#
#     def __add__(self, other):
#         if isinstance(other, Earth):
#             return Clay
#         elif isinstance(other, Water):
#             return Dust
#
# class Earth:
#     image = PhotoImage(file='ground.png').subsample(4, 4)
#
#     def __add__(self, other):
#         if isinstance(other, Fire):
#             return Clay
#         elif isinstance(other, Water):
#             return Flag
#         elif isinstance(other, Wind):
#             return Gory
#
#
# class Wind:
#     image = PhotoImage(file='wind.png').subsample(4, 4)
#     def __add__(self, other):
#         if isinstance(other, Earth):
#             return Gory
#
#
# class Water:
#     image = PhotoImage(file='water.png').subsample(4, 4)
#     def __add__(self, other):
#         if isinstance(other, Fire):
#             return Dust
#         elif isinstance(other, Earth):
#             return Flag
#
# class Clay:
#     image = PhotoImage(file='pottery.png').subsample(4, 4)
#
# class Dust:
#     image = PhotoImage(file='dust.png').subsample(4, 4)
#
#
# class Flag:
#     image = PhotoImage(file='flag-kazakhstana.png').subsample(4, 4)
#
# class Gory:
#     image = PhotoImage(file='gory.png').subsample(4, 4)
#
#
# def move(event):
#     images_id = canvas.find_overlapping(event.x, event.y, event.x + 10, event.y + 10)
#     if len(images_id) == 2:
#         elem_1 = elements[images_id[0] - 1]
#         elem_2 = elements[images_id[1] - 1]
#         new_elem = elem_1 + elem_2
#         if new_elem not in elements:
#             elements.append(new_elem)
#             canvas.create_image(event.x, event.y, image=new_elem.image)
#     canvas.coords(images_id, event.x, event.y)
#
# elements = [Fire(), Water(), Earth(), Wind()]
# for elem in elements:
#     canvas.create_image(randint(50, 350), randint(50, 350), image=elem.image)
#
# window.bind('<B1-Motion>', move)
#
# window.mainloop()

# goods = [
#     {
#         'name': 'iphone 10',
#         'brand': 'aplle',
#         'price': 50_000
#     },
#     {
#         'name': 'readme pro+ extreme Pro 9',
#         'brand': 'xiaomi',
#         'price': 10_000
#     },
#     {
#         'name': 'sasung',
#         'brand': 'sas',
#         'price': 56_000
#     }
# ]
# def item_price(item):
#     return item['price']
#
#
#
# print(sorted(goods, key=lambda item: item['price']))

# apple = list(filter(lambda item: item['brand'] == 'aplle', goods))
# print(apple)

# def strcounter(s):
#     sym_dict = {}
#     for item in s:
#         sym_dict[item] = 1 + sym_dict.get(item, 0)
#
#     for item, count in sym_dict.items():
#         print(f'{item} - {count}')
#
#
# strcounter('asfgnas')

# import random

# def palindrom(s):
#     return s[::-1] == s
#
# while True:
#     s = input('Введите слово: ')
#     print(f'{s} являеться палиндромом' if palindrom(s) else 'Не палиндром')
#

# lst = []
# lst_2 = []
# for i in range(1, 1001):
#     lst.append(i)
#
# for i in lst:
#     if i % 3 == 0:
#         lst_2.append(i)
#
# print(sum(lst_2))

# import random
# def love():
#     men = random.randint(8, 9)
#     woman = random.randint(8, 9)
#     if men != woman:
#         print('True')
#     else:
#         print('False')
#
# love()
# def reverse_words(text):

# lst_x = []
# lst_p = []
# lst_d = []
# g = 0
# a = int(input('Сколько чисел: '))
# for i in range(a):
#     d = input('Введите число х: ')
#     b = input('Введите число р: ')
#     c = int(d) * b
#     lst_d.append(c)
# for i in lst_d:
#     g += float(i)
#
# print(g)

# def Work_2():                      # Номер 5 дз
#     for x in range(0, 2):
#         for y in range(0, 2):
#             for z in range(0, 2):
#                 for w in range(0, 2):
#                     if (x or (not(z))) and (x == (not(w))) and ((not(x)) or y):
#                         print(x, y, z, w)
# Work_2()

# def Work_2():                      # Номер 6 дз
#     for x in range(0, 2):
#         for y in range(0, 2):
#             for z in range(0, 2):
#                 for w in range(0, 2):
#                     if (x or y) and ((not(y)) != (not(z))) and not(w):
#                         print(x, y, z, w)
# Work_2()

# def Work_2():                      # Номер 7 дз   Спросить насчет 7 задания насчет начала в решении и у меня ( not )
#     for x in range(0, 2):
#         for y in range(0, 2):
#             for z in range(0, 2):
#                 for w in range(0, 2):
#                     if (not(x == (not(y))) or ((x and w) == (z and (not(w))))) == False:
#                         print(x, y, z, w)
# Work_2()

# def Work_2():                      # Номер 8 дз
#     for x in range(0, 2):
#         for y in range(0, 2):
#             for z in range(0, 2):
#                 for w in range(0, 2):
#                     if (y and ((not(x)) != (not(w))) and ((not(z)) or x)):
#                         print(x, y, z, w)
# Work_2()

# Домашнее задание 1. 11) 2. 24) 3. 20) 4. 15) 5. wyzx) 6. xzyw) 7. Нужно узнать) 8. zxyw)

# def Work_2():                      # Номер 8 дз
#     for x in range(0, 2):
#         for y in range(0, 2):
#             for z in range(0, 2):
#                 for w in range(0, 2):
#                     if (((y <= x) and (z or w)) <= ((x and (not(w))) or (y == z))) == False:
#                         print(x, y, z, w)
# Work_2()
#
# def Work_2():                      # Номер 8 дз
#     for x in range(0, 2):
#         for y in range(0, 2):
#             for z in range(0, 2):
#                 for w in range(0, 2):
#                     if (w <= (y == z)) and (y == (z <= x)):
#                         print(x, y, z, w)
# Work_2()

# count = 0                                                           # Решение задачи дз от репетитора
# lst = [i for i in range(245690,245757)]
# def prost(lst):
#     for a in lst:
#         count = 0
#         for i in range(2, a // 2+1):
#             if a % i == 0:
#                 count += 1
#         if count <= 0:
#             print(f'{lst.index(a) + 1} {a}')
# prost(lst)


# a = int(input("Введите число: "))
# k = 0
# for i in range(2, a // 2+1):
#     if (a % i == 0):
#         k = k+1
# if (k <= 0):
#     print("Число простое")
# else:
#     print("Число не является простым")
#












