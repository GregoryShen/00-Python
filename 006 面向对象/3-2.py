class Programmer:
    hobby = 'Play Computer'

    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    def get_weight(self):
        return self.__weight


if __name__ == '__main__':
    programmer = Programmer('Albert', 25, 80)
    print(dir(programmer))
    print(programmer.__dict__)
    programmer.get_weight()
    print(programmer._Programmer__weight)
