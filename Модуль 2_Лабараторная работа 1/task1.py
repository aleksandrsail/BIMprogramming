# TODO Написать 3 класса с документацией и аннотацией типов

import doctest

class Script:
    def __init__(self, author: str, name: str, pages: int, last_read_page: int):
        """
        Создание и подготовка к работе объекта «Сценарий»
        :param author: Автор сценария
        :param name: Название пьесы
        :param pages: Количество страниц в сценарии
        :param last_read_page: Значение последней прочитанной страницы

        Пример:
        >>> script = Script('Чехов', 'Вишнёвый сад', 112, 12)
        """

        self.author = author
        self.name = name
        self.pages = pages
        self.last_read_page = last_read_page

    def increment_last_read_page(self, read_pages: int):
        """
        Функция, которая добавляет прочитанные страницы
        :param read_pages: Количество прочитанных страниц

        Примеры:
        >>> script = Script('Чехов', 'Вишнёвый сад', 112, 12)
        >>> script.increment_last_read_page(100)
        """

        if not isinstance(read_pages, int):
            raise TypeError('Количество страниц должно быть типа int')
        if read_pages < 0:
            raise ValueError('Количество страниц должно быть положительным числом')
        if self.last_read_page + read_pages > self.pages:
            raise ValueError('Количество страниц превышает общее количество')

        self.last_read_page += read_pages

    def decrement_last_read_page(self, backwards_pages: int):
        """
        Функция, которая перелистывает страницы обратно
        :param backwards_pages: Количество перелистнутых страниц

        Примеры:
        >>> script = Script('Чехов', 'Вишнёвый сад', 112, 60)
        >>> script.decrement_last_read_page(40)
        """
        if not isinstance(backwards_pages, int):
            raise TypeError('Количество страниц должно быть типа int')
        if backwards_pages < 0:
            raise ValueError('Количество страниц должно быть положительным числом')
        if self.last_read_page - backwards_pages < 0:
            raise ValueError('Окончательное количество страниц отрицательно')

        self.last_read_page -= backwards_pages


class Cat:
    def __init__(self, name: str, age: int, happy: bool, weight: int):
        """
        Создание и подготовка к работе объекта «Кот»
        :param name: кличка кота
        :param age: возраст кота
        :param happy: является ли кот счастливым
        :param weight: вес кота

        Пример:
        >>> cat = Cat('Мурзик', 4, True, 10)
        """

        self.name = name
        self.age = age
        self.happy = happy
        self.weight = weight

    def diet_routine(self, plan_weight: int):
        """
        Установление диеты
        :param plan_weight: плановый вес кота
        :raise ValueError: если вес кота опустится ниже допустимых значений
        :return: текущий вес кота

        Пример:
        >>> cat = Cat('Мурзик', 4, True, 10)
        >>> cat.diet_routine(10)
        """

        if not isinstance(plan_weight, int):
            raise TypeError('Плановый вес должен быть типа int')
        if plan_weight < 0:
            raise ValueError('Плановый вес должен быть неотрицательным числом')
        self.weight = plan_weight

    def feed_the_cat(self, added_weight: int):
        """Покормить кота
        :param added_weight: на сколько потолстеет кот
        :return: текущий вес кота

        Пример:
        >>> cat = Cat('Мурзик', 4, True, 10)
        >>> cat.feed_the_cat(1)"""

        if not isinstance(added_weight, int):
            raise TypeError('Добавленный вес должен быть типа int')
        if added_weight < 0:
            raise ValueError('Добавленный вес должен быть неотрицательным числом')

        self.weight += added_weight


class Car:
    def __init__(self, model, year, speed=0):
        """
        Создание и подготовка к работе объекта «Машина»
        :param model: модель машины
        :param year: год выпуска
        :param speed: текущая скорость

        Пример:
        >>> car = Car('Mitsubishi Lancer', 2012, 10)
        """
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self, amount):
        """
        Ускорение машины
        :param amount: величина ускорения
        :return: значение скорости машины
        """
        if not isinstance(amount, int):
            raise TypeError('Ускорение должно быть типа int')
        if amount < 0:
            raise ValueError('Ускорение должно быть неотрицательным числом')
        self.speed += amount

    def brake(self, amount):
        """
        Замедление машины
        :param amount: величина замедления
        :return: значение скорости машины
        """
        if not isinstance(amount, int):
            raise TypeError('Замедление должно быть типа int')
        if amount < 0:
            raise ValueError('Замедление должно быть неотрицательным числом')
        if self.speed - amount < 0:
            self.speed = 0
        else:
            self.speed -= amount


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass
