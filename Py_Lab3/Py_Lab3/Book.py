from abc import abstractmethod


class Taggable:

    @abstractmethod
    def tag(self):
        pass


class Book(Taggable):

    def __init__(self, author, name):
        self.__author = author
        self.__name = name
        self._id = 0

        if name == '' or author == '':
            raise ValueError('error')

    def __str__(self):
        return "%s '%s'" % (self.__author, self.__name)

    def tag(self):
        keys = self.__name.replace(',', ' ').split()
        return [word for word in keys if word.istitle()]



