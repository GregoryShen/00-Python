from contextlib import contextmanager


class Query:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print("Query info about %s" % self.name)


# with Query('Bob') as q:
#     q.query()

# 对上述Query类用contextmanager进行改写

class Query1:
    def __init__(self, name):
        self.name = name

    def query(self):
        print("Query1 info about %s" % self.name)


@contextmanager
def create_query(name):
    print('Begin')
    q1 = Query1(name)
    yield q1
    print('End')


# with create_query('Alice') as q:
#     q.query()


# 很多时候我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)


# with tag("h1"):
#     print("Hello")
#     print("world")

# 如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用closing()来把该对象变为
# 上下文对象。
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen("https://www.python.org")) as page:
    for line in page:
        print(line)


# closing也是一个经过@contextmanager装饰的生成器，这个生成器编写起来非常简单
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()