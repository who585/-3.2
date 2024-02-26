class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author
    @property
    def name(self)->str:
        return self.name
    @property
    def author(self)->str:
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name,author)
        self.pages = pages
    @property
    def pages(self)->str:
        return self.pages
    @pages.setter
    def pages(self, new_pages: int)->None:
        if not isinstance(new_pages, int):
            raise TypeError("Страницы должны быть типа int")
        if new_pages <= 0:
            raise ValueError("Странциы должны быть положительным числом")
        self.pages = new_pages

    def __str__(self):
        return f"Бумажная книга {self.name}. Автор {self.author}. Количество станиц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность должна быть типа float")
        if new_duration <= 0:
            raise ValueError("Продолжительность  должна быть положительным числом")
        self._duration = new_duration

    def __str__(self):
        return f"Аудиокнига {self.name}. Автор {self.author}. Продолжительность {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration = {self.duration})"