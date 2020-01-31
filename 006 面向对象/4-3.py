class Programmer:
    def __init__(self, name, age):
        self.name = name
        if isinstance(age, int):
            self.age = age
        else:
            raise Exception('age must be int')

    def __eq__(self, other):
        if isinstance(other, Programmer):
            if self.age == other.age:
                return True
            else:
                return False
        else:
            raise Exception('The type of object must be Programmer')

    def __add__(self, other):
        if isinstance(other, Programmer):
            return self.age + other.age
        else:
            raise Exception('The type of object must be Programmer')


if __name__ == '__main__':
    p1 = Programmer('Albert', 25)
    p2 = Programmer('Bill', 30)
    print(p1 == p2)
    print(p1 + p2)
