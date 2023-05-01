from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра класса Phone.
        :param number_of_sim: Количество поддерживаемых сим-карт.
        """
        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim

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
        return f"{super().__repr__()}, {self._number_of_sim})"

    def __str__(self) -> str:
        return f'{super().__str__()}'
