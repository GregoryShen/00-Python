# import os
#
# try:
#     f = open('F.txt')
#     print("in try -> f.read():", f.read())
#     f.seek(-5, os.SEEK_SET)
# except IOError as e:
#     print("Catch IOError:", e)
# except ValueError as e:
#     print("Catch ValueError:", e)
# finally:
#     f.close()
# print("try-finally: ", f.closed)

# with open('F.txt') as f1:
#     print('in with -> f1.read():', f1.read())
#     f1.seek(-5, os.SEEK_SET)
# print("with: ", f1.closed)

# try:
#     with open('F.txt') as f1:
#         print("in with f1.read():", f1.read())
#         f.seek(-5, os.SEEK_SET)
# except ValueError as e:
#     print("in with catch ValueError:", e)
#     print("with:", f1.closed)


class MyContext:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print("__enter__")
        return self

    def do_self(self):
        print("do_self")
        a

    def __exit__(self, exc_type, exc_value, traceback):
        print("__exit__")
        print("Error:", exc_type, " info:", exc_value)


if __name__ == '__main__':
    with MyContext('test context') as f:
        print(f.name)
        f.do_self()
