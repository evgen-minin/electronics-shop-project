from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра класса Phone.
        :param number_of_sim: Количество поддерживаемых сим-карт.
        """
        super(Phone, self).__init__(name, price, quantity)
        self._number_of_sim = number_of_sim

    @property
    def number_of_sim(self) -> int:
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Количество физических SIM-карт должно быть целым числом.")
        if value <= 0:
            raise ValueError("Количество физических SIM-карт должно быть больше нуля.")
        self._number_of_sim = value

    def __repr__(self) -> str:
        return f"{super().__repr__()}, {self._number_of_sim})"

    def __str__(self) -> str:
        return f'{super().__str__()}'

    def __add__(self, other):
        if isinstance(other, Phone):
            return super().__add__(other)
        raise TypeError("Можно складывать только экземпляры классов Item и Phone")
