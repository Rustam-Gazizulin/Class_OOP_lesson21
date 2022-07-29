from abc import ABC, abstractproperty, abstractmethod


class BaseCourse(ABC):
    @property
    @abstractmethod
    def title(self):
        pass

    @property
    @abstractmethod
    def description(self):
        pass

    @property
    @abstractmethod
    def credit(self):
        pass


class Course(BaseCourse):
    def __init__(self, title, description, credit):
        self._title = title
        self._description = description
        self._credit = credit

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description()

    @property
    def credit(self):
        return self._credit()


course = Course('Title', 'Description content', 34)
