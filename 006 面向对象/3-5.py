class Programmer:
    hobby = 'Play Computer'

    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    @classmethod
    def get_hobby(cls):
        return cls.hobby

    @property
    def get_weight(self):
        return self.__weight

    def self_introduction(self):
        print('My name is {}\nI am {} years old\n'.format(self.name, self._age))


class BackendProgrammer(Programmer):
    def __init__(self, name, age, weight, language):
        super(BackendProgrammer, self).__init__(name, age, weight)
        self.language = language

    def self_introduction(self):
        print('My name is {}\nMy favourite language is {}'.format(self.name, self.language))


def introduce(p):
    if isinstance(p, Programmer):
        p.self_introduction()


if __name__ == '__main__':
    programmer = Programmer('Albert', 25, 80)
    backend_programmer = BackendProgrammer('Tim', 30, 70, 'Python')
    introduce(programmer)
    introduce(backend_programmer)
