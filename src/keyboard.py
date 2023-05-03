from src.item import Item


class LanguageMixin:
    """
    Класс миксин, реализующий метод для изменения языка клавиатуры
    """

    def __init__(self, language: str = 'EN') -> None:
        self.language = language

    def change_lang(self):
        """
        Метод для изменения языка клавиатуры
        """
        if self.language == 'EN':
            self.language = 'RU'
        else:
            self.language = 'EN'
        return self


class KeyBoard(Item, LanguageMixin):
    """
    Класс представляющий товар "клавиатура"
    """

    def __init__(self, name: str, price: float, quantity: int, language: str = "EN") -> None:
        super().__init__(name, price, quantity)
        self.__language = language

    @property
    def language(self) -> str:
        """
        Геттер для атрибута  language.
        """

        return self.__language

    def change_lang(self):
        """
        Метод для изменения языка клавиатуры.
        """
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self
