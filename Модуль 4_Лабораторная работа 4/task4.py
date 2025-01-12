class Transport:
    def __init__(self, brand: str, model: str, year: int, color: str):
        """
        Создание и подготовка к работе объекта «Транспорт»

        :param brand: Бренд.
        :param model: Модель.
        :param year: Год выпуска.
        :param color: Цвет.
        """
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def move(self, speed: int) -> str:
        """
        Метод, описывающий скорость движения транспорта.

        :param speed: Скорость движения в км/ч.
        :return: Строка с описанием движения.
        """
        return f"{self.brand} {self.model} движется со скоростью {speed} км/ч."

    def __str__(self) -> str:
        """
        Магический метод для представления в текстовой форме.

        :return: Строка о транспорте.
        """
        return f"{self.year} {self.color} {self.brand} {self.model}"

    def __repr__(self) -> str:
        """
        Магический метод для внутреннего представления объекта.

        :return: Строка о транспорте.
        """
        return f"Transport(brand='{self.brand}', model='{self.model}', year={self.year}, color='{self.color}')"


class Car(Transport):
    def __init__(self, brand: str, model: str, year: int, color: str, num_doors: int):
        """
        Создание и подготовка к работе дочернего класса "Легковой автомобиль".

        :param brand: Бренд.
        :param model: Модель.
        :param year: Год выпуска.
        :param color: Цвет.
        :param num_doors: Количество дверей.
        """
        super().__init__(brand, model, year, color)
        self.num_doors = num_doors

    def start_engine(self) -> str:
        """
        Метод, описывающий запуск двигателя.

        :return: Строка о запуске двигателя.
        """
        return f"{self.brand} {self.model} завелся."

    def __str__(self) -> str:
        """
        Перегрузка магического метода для получения строки с объектом в текстовой форме.

        :return: Строка с информацией.
        """
        return f"{super().__str__()}, {self.num_doors} дверей"

    def __repr__(self) -> str:
        """
        Перегрузка магического метода для получения строки для внутреннего представления.

        :return: Строка с информацией.
        """
        return f"Car(brand='{self.brand}', model='{self.model}', year={self.year}, color='{self.color}', num_doors={self.num_doors})"


if __name__ == "__main__":
    # Примеры использования классов
    car1 = Car(brand="Hongqi", model="H9", year=2023, color="Black", num_doors=4)
    print(car1.move(90))  # Вывод: Hingqi H9 движется со скоростью 90 км/ч.
    print(car1.start_engine())  # Вывод: Hingqi H9 завелся.
    print(str(car1))  # Вывод: 2023 Black Hingqi H9, 4 дверей
    print(repr(car1))  # Вывод: Car(brand='Hingqi', model='H9', year=2023, color='Black', num_doors=4)
    pass