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
        print('My name is {}\nI am {} years old'.format(self.name, self._age))


if __name__ == '__main__':
    programmer = Programmer('Albert', 25, 80)
    print(dir(programmer))
    print(Programmer.hobby)
    print(programmer.get_weight)
    programmer.self_introduction()
