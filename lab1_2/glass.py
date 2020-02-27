# -*- coding: utf-8

#
# Курс DEV-PY200. Объектно-ориентированное программирование на языке Python
# Тема 1.1 Основы ООП. Понятие класса, объекта. Создание экземпляра класса

# Лабораторная работа № 1.1 (4 ак.ч.)

# Слушатель (ФИО): TILLOEV TILLO ABDULLOEVICH

# ---------------------------------------------------------------------------------------------
# Понятие класса, объекта (стр. 1-22)

# 1. Создайте класс Glass с атрибутами capacity_volume и occupied_volume
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)
print("ЗАДАНИЕ 1")
class Glass:
    def __init__(self, capacity_volume, occupied_volume):
        if isinstance(capacity_volume, (int, float)):
            if capacity_volume > 0:
                self.capacity_volume = capacity_volume
            else:
                raise ValueError
        else:
            raise TypeError
        if isinstance(capacity_volume, (int, float)):
            if occupied_volume >= 0:
                self.occupied_volume = occupied_volume
            else:
                raise ValueError
        else:
            raise TypeError

    def get_self_id (self):
        return hex(id(self))

    print("EXERCISES DONE", "\n")


# 2. Создайте два и более объектов типа Glass
#    Измените и добавьте в любой стакан любое кол-во воды (через атрибуты)
#    Убедитесь, что у других объектов Glass атрибуты экземпляра класса не изменились.
print("ЗАДАНИЕ 2")
# TODO glass_2_1, glass_2_2, glass_2_3 GlassDefaultArg (200, 100)
g2_1 = Glass(200, 12)
print(f"Glass Volume 1: {g2_1.capacity_volume}, Volume water in Glass 1: {g2_1.occupied_volume}")

g2_2 = Glass(100, 0)
print(f"Volume of Glass 2: {g2_2.capacity_volume}, Volume water in Glass 2: {g2_2.occupied_volume}")
print("EXERCISES DONE", "\n")


# 3. Создайте класс GlassDefaultArg (нужен только __init__) c аргументом occupied_volume
#    По умолчанию occupied_volume равен нулю. Создайте два объекта с 0 и 200
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)
print("ЗАДАНИЕ 3")
class GlassDefaultArg:
    def __init__(self, capacity_volume, occupied_volume=0):
        if isinstance(capacity_volume, (int, float)):
            if capacity_volume > 0:
                self.capacity_volume = capacity_volume
            else:
                raise ValueError
        else:
            raise TypeError
        if isinstance(capacity_volume, (int, float)):
            if occupied_volume >= 0:
                self.occupied_volume = occupied_volume
            else:
                raise ValueError
        else:
            raise TypeError


#glass_3_1 = GlassDefaultArg(200)
#glass_3_2 = GlassDefaultArg(200, 100)

g3_1 = GlassDefaultArg(200)
print(f"Volume of Glass 1: {g3_1.capacity_volume}, Volume coffe in Glass 1: {g3_1.occupied_volume}")

g3_2 = GlassDefaultArg(200, 200)
print(f"Volume of Glass 2: {g3_1.capacity_volume}, Volume coffe in Glass 2: {g3_1.occupied_volume}")
print("EXERCISES DONE", "\n")


# 4. Создайте класс GlassDefaultListArg (нужен только __init__)
#    c аргументами capacity_volume, occupied_volume.
#    Пусть аргументом по умолчанию для __init__ occupied_volume = []. Будет список.
#    Попробуйте создать 3 объекта, которые изменяют occupied_volume.append(2) внутри __init__.
#    Создавайте объект GlassDefaultListArg только с одним аргументом capacity_volume.
#    Опишите результат.
#    Подсказка: можно ли использовать для аргументов по умолчанию изменяемые типы?

class GlassDefaultListArg:
    def __init__(self, capacity_volume, occupied_volume=[]):
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume
        self.occupied_volume.append(2)


print("ЗАДАНИЕ 4")
print("version 1")
glass_4_1 = GlassDefaultListArg(100)
print("glass_4_1.occupied_volume: --->", glass_4_1.occupied_volume)

glass_4_2 = GlassDefaultListArg(200)
print("glass_4_1.occupied_volume: --->", glass_4_2.occupied_volume)

glass_4_2 = GlassDefaultListArg(300)
print("glass_4_1.occupied_volume: --->", glass_4_2.occupied_volume)
print("V1 EXERCISES DONE", "\n")

class GlassDefaultListArgV2:
    def __init__(self, capacity_volume, occupied_volume=[]):
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume
        #self.occupied_volume.append(2)


hashtagOne = "# нельзя использовать для аргументов по умолчанию изменяемые типы"
hashtagTwo = "# при запуске возникает ошибка AttributeError"
print("\n", "version 2", "\n", hashtagOne, "\n", hashtagTwo )

glass_4_1v2 = GlassDefaultListArgV2(200)
print(f"Volume of Glass 1: {glass_4_1v2.capacity_volume}, Volume coffe in Glass 1: {glass_4_1v2.occupied_volume}")
glass_4_2v2 = GlassDefaultListArgV2(200, 50)
print(f"Volume of Glass 2: {glass_4_2v2.capacity_volume}, Volume coffe in Glass 2: {glass_4_2v2.occupied_volume}")
glass_4_3v2 = GlassDefaultListArgV2(200, 150)
print(f"Volume of Glass 3: {glass_4_3v2.capacity_volume}, Volume coffe in Glass 3: {glass_4_3v2.occupied_volume}")
print("V2 EXERCISES DONE", "\n")
# нельзя использовать для аргументов по умолчанию изменяемые типы
# при запуске возникает ошибка AttributeError


# 5. Создайте класс GlassAddRemove, добавьте методы add_water, remove_water
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)
#    Вызовите методы add_water и remove.
#    Убедитесь, что методы правильно изменяют атрибут occupied_volume.
class GlassAddRemove:
    def __init__(self, capacity_volume, occupied_volume):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        elif capacity_volume <= 0:
            raise ValueError
        else:
            self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        elif occupied_volume < 0:
            raise ValueError
        elif occupied_volume > capacity_volume:
            raise ValueError
        else:
            self.occupied_volume = occupied_volume

        self.ostatok = None


    def add_water(self, adding_water):
        if not isinstance(adding_water, (int, float)):
            raise TypeError

        space = self.capacity_volume - self.occupied_volume
        if space < adding_water:
            self.occupied_volume += space
            self.ostatok = adding_water - space
            return self.ostatok
        else:
            self.occupied_volume += adding_water

    def remove_water(self, remove_water):
        if not isinstance(remove_water, (int, float)):
            raise TypeError

        if remove_water >= self.occupied_volume:
            self.occupied_volume = 0
        else:
            self.occupied_volume -= remove_water


print("ЗАДАНИЕ 5")
glass_5_1 = GlassAddRemove(200, 100)
glass_5_1.add_water(100)

print(glass_5_1, "\n")

# проверка добавления/удаления воды
stakan = GlassAddRemove(200, 50)
print(f"Volume of glass: {stakan.capacity_volume}, Volume coffe in glass: {stakan.occupied_volume}")

stakan.add_water(200)  # добавление воды в стакан
print(f"Volume coffe in glass after adding: {stakan.occupied_volume}")
print(f"Остаток воды на счёте: {stakan.ostatok}")

stakan.remove_water(50)  # удаление воды из стакана
print(f"Volume coffe in glass after removing: {stakan.occupied_volume}")

stakan.remove_water(200)
print(f"Volume coffe in glass after rm again: {stakan.occupied_volume}")
print("EXERCISES DONE", "\n")

# 6. Создайте три объекта типа GlassAddRemove,
#    вызовите функцию dir для трёх объектов и для класса GlassAddRemove.
#    а. Получите типы объектов и класса
#    б. Проверьте тип созданного объекта.

print("ЗАДАНИЕ 6")
glass_6_1 = GlassAddRemove(200, 100)
print("type(glass_6_1): --->", type(glass_6_1))
glass_6_2 = GlassAddRemove(500, 50)
print("type(glass_6_2): --->", type(glass_6_2))
glass_6_3 = GlassAddRemove(100, 0)
print("type(glass_6_3): --->", type(glass_6_3), "\n")

print("type(GlassAddRemove): --->", type(GlassAddRemove), "\n")

print("DIR: --->", dir(glass_6_1))
print("EXERCISES DONE", "\n")




# ---------------------------------------------------------------------------------------------
# Внутренние объекты класса (стр. 25-33)

# 7. Получите список атрибутов экземпляра класса в начале метода __init__,
#    в середине __init__ и в конце __init__, (стр. 28-30)
#    а также после создания объекта.
#    Опишите результат.

print("ЗАДАНИЕ 7")


class GlassDir:
    def __init__ (self, v, s):
        print(dir(self))
        print(self.__dict__)

        self.v = v
        # print(dir(self))
        print(self.__dict__)

        self.s = s
        # print(dir(self))
        print(self.__dict__)

a = GlassDir(1, 15)
print("EXERCISES DONE", "\n")

# 8. Создайте три объекта Glass. (стр. 27)
#    Получите id для каждого объекта с соответсвующим id переменной self.

print()
print("ЗАДАНИЕ 8")
glass_8_1 = Glass(200, 100)
print("hex(id(glass_8_1)): --->", hex(id(glass_8_1)))
print("glass_8_1.get_self_id(): --->", glass_8_1.get_self_id(), "\n")

# 9. Корректно ли следующее объявление класса с точки зрения:
#     - интерпретатора Python;
#     - соглашения о стиле кодирования
#    Запустите код.


print("ЗАДАНИЕ 9", "\n", "NO ERROR FOUND")
class d:
    def __init__(f, a=2):
        f.a = a

    def print_me(p):
        print("p.a ------>", p.a, "\n")

d.print_me(d())



# 10. Исправьте

print("ЗАДАНИЕ 10")
class A:
    def __init__(self, a):
        self.a = a;
        if 10 < a < 50:
            return

print("A(30): -------->", A(30), "\n")

# Объясните так реализовывать __init__ нельзя?


# 11. Циклическая зависимость (стр. 39-44)
#
print("ЗАДАНИЕ 11")
# TODO check link: http://py-algorithm.blogspot.com/2011/08/blog-post.html  for help
# please check file exercise11



class Node:
    def __init__(self, prev=None, next_=None):
        self.__prev = prev
        self.__next = next_

    def set_next(self, next_):
        self.__next = next_

    def set_prev(self, prev):
        self.__prev = prev

    def __str__(self):
        ...

    def __repr__(self):
        ...


class LinkedList:
    def __init__(self, nodes=None):
        if nodes is None:
            self.head = None
            self.tail = None
        elif isinstance(nodes, Node):
            self.head = nodes
            self.tail = nodes
        elif isinstance(nodes, list):
            self.head = nodes[0]
            self.tail = nodes[-1]
            self.linked_nodes(nodes)

    def linked_nodes (self, nodes):
        nodes[0].set_prev(nodes[-1])
        nodes[0].set_next(nodes[1])

        for i in range (1, len(nodes) - 1):
            nodes[i].set_prev(nodes[i-1])
            nodes[i].set_next(nodes[i + 1])

        nodes[-1].set_prev(nodes[-2])
        nodes[-1].set_next(nodes[0])


    def insert(self, node, index=0):
        '''
        Insert Node to any place of LinkedList
        node - Node
        index - position of node
        '''
        ...

    def append(self, node):
        '''
        Append Node to tail of LinkedList
        node - Node
        '''
        ...

    def clear(self):
        '''
        Clear LinkedList
        '''
        ...

    def find(self, node):
        ...

    def remove(self, node):
        ...

    def delete(self, index):
        ...
























