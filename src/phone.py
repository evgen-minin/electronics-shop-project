class Phone:
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра класса Phone.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param number_of_sim: Количество поддерживаемых сим-карт.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if not isinstance(value, int):
            raise TypeError("Количество физических SIM-карт должно быть целым числом.")
        if value <= 0:
            raise ValueError("Количество физических SIM-карт должно быть больше нуля.")
        self._number_of_sim = value

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self) -> str:
        return f'{self.name}'

    def __add__(self, other):
        return self.quantity + other.quantity
