class Programmer:

    def __new__(cls, *args, **kwargs):
        print('call __new__ method')
        print('args: ', args)
        print()
        return super(Programmer, cls).__new__(cls)

    def __init__(self, name, age):
        print('call __init__ method')
        self.name = name
        self.age = age


if __name__ == '__main__':
    programmer = Programmer('Albert', 25)
    print()
    print('__dict__: ', programmer.__dict__)
