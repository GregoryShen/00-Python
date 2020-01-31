class Programmer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getattribute__(self, key):
        return super(Programmer, self).__getattribute__(key)
        # return getattr(self, key)
        # return self.__dict__[key]

    def __setattr__(self, key, value):
        # setattr(self, key, value)
        self.__dict__[key] = value

if __name__ == '__main__':
    p = Programmer('Albert', 25)
    print(p.name)