# [廖雪峰:contextlib](https://www.liaoxuefeng.com/wiki/1016959663602400/1115615597164000)

## 关闭文件时的例子

在Python中,读写文件这样的资源要特别注意,必须在使用完毕后正确关闭它们.正确关闭文件资源的一个方法是使用`try…finally`:

```python
try:
    f = open('/path/to/file', 'r')
    f.read()
finally:
    if f:
        f.close()
```

写`try…finally`非常繁琐.Python的with语句允许我们非常方便地使用资源,而不必担心资源没有关闭,所以上面的代码可以简化为:

```python
with open('/path/to/file', r) as f:
    f.read()
```

并不是之后`open()`函数返回的fp对象才能使用`with`语句.实际上,任何对象,只要正确实现了==上下文管理==,就可以用于`with`语句.

## 上下文管理的实现

实现上下文管理是通过`__enter__`和`__exit__`这两个方法实现的.例如,下面的class实现了这两个方法:

```python
class Query(object):
  
  	def __init__(self, name):
        self.name = name
      
    def __enter__(self):
        print('Begin')
        return self
      
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')
            
    def query(self):
      print('Query info about %s...' % self.name)
```

这样我们就可以把自己写的资源对象用于`with`语句:

```python
with Query('Bob') as q:
    q.query()
```

## @contextmanager

编写`__enter__`和`__exit__`仍然很繁琐,因此Python的标准库`contextlib`提供了更简单的写法,上面的代码可以改写如下:

```python
from contextlib import contextmanager

class Query(object):
  
    def __init(self, name):
        self.name = name
        
    def query(self):
        print('Query info about %s...' % self.name)
        
        
@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')
```

`@contextmanager`这个装饰器接受一个生成器,用`yield`语句把`with … as var`把变量输出出去,然后,`with`语句就可以正常的工作了:

```python
with create_query('Bob') as q:
    q.query()
```

很多时候,我们希望在某段代码执行后自动执行特定代码,也可以用`@contextmanager`实现.例如:

```python
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)
    
with tag("h1"):
    print("hello")
    print("world")
```

上述代码执行结果为:

```python
<h1>
hello
world
</h1>
```

代码的执行顺序是:

1. `with`语句首先执行`yield`之前的语句,因此打印出`<h1>`
2. `yield`调用会执行`with`语句内部的所有语句,因此打印出`hello`和`world`
3. 最后执行`yield`之后的语句,打印出`</h1>`

因此,`@contextmanager`让我们通过编写生成器来简化上下文管理

## @closing

如果一个对象没有实现上下文,我们就不能把它用于`with`语句.这个时候,可以用`closing()`来把该对象变为上下文对象.例如,用`with`语句使用`urlopen()`:

```python
from contextlib import closing
import urllib

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)
```

`closing`也是一个经过@contextmanager装饰的生成器,这个生成器编写起来非常简单:

```python
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
```

它的作用就是把任意对象变为上下文对象,并支持`with`语句

@contextlib还有一些其他装饰器,便于我们编写更简洁的代码.



# [PythonDoc: contextlib](https://docs.python.org/3/library/contextlib.html)

**Source code:** Lib/contextlib.py

----

This module provides utilities for common tasks involving the `with` statement. For more information see also `Context Manager Types` and `With Statement Context Managers`.

## Utilities

Functions and classes provided:

### @contextlib.**contextmanager**

This function is a decorator that can be used to define a factory function for `with` statement context managers, without needing to create a class or separate `__enter__()` and `__exit__()` methods.

While many objects natively support use in with statements, sometimes a resource need to be managed that isn’t a context manager in its own right, and doesn’t implement a `close()` method for use with `context lib.closing`

An abstract example would be the following to ensure correct resource management:

```python
from contextlib import contextmanager

@contextmanager
def managed_resource(*args, **kwds):
    # Code to acquire resource, e.g.:
    resource = acquire_resource(*args, **kwds)
    try:
        yield resource
    finally:
        # Code to release resource, e.g.:
        release_resource(resource)
        
>>> with managede_resource(timeout=3600) as resource:
...     # Resource is released at the end of this block,
...     # even if code in the block raises an exception
```

The function being decorated must return a generator-iterator when called. This iterator must yield exactly one value, which will be bound to the targets in the with statement’s as clause, if any.

At the point where the generator yields, the block nested in the `with` statement is executed. The generator is then resumed after the block is exited. If an unhandled exception occurs in the block, it is reprised inside the generator at the point where the yield occurred. Thus, you can use a `try…except…finally` statement to  trap the error(if any), or ensure that some cleanup takes place. If an exception is trapped merely in order to log it or to perform some action(rather than to suppress it entirely), the generator must reraise that exception. Otherwise the generator context menager will indicate to the with statement that the exception has been handled, and execution will resume with the statement immediately following the `with` statement.

`contextmanager()` uses `ContextDecorator` so the context managers it creates can be used as decorators as well as in `with` statements. When used as a decorator, a new generator instance is implicitly created on each function call (this allows the otherwise “one-shot” context managers created by `contextmanager()` to meet the requirement that context managers support multiple invocations in order to be used as decorators.)

### contextlib.**closing**(*thing*)

Return a context manager that closes *thing* upon completion of the block. This is basicaly equivalent to:

```python
from contextlib import contextmanager

@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
```

And lets you write code like this:

```python
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)
```

without needing to explicitly close `page`. Even if an error occurs, `page.close()`will be called when the `with` block is exited.

# [contextlib 掘金](https://juejin.im/post/5c7b462cf265da2d97110f50)

用于创建和使用上下文管理器的实用程序

`contextlib`模块包含用于处理上下文管理器和`with`语句的实用程序.



# [with语句、context manager类型和contextlib库](https://www.cnblogs.com/Security-Darren/p/4196634.html)



# [谈一谈Python的上下文管理器](http://www.bjhee.com/python-context.html)



# [with语句与上下文管理器](https://www.cnblogs.com/nnnkkk/p/4309275.html)



# [浅谈 Python 的 with 语句]([https://www.ibm.com/developerworks/cn/opensource/os-cn-pythonwith/index.html?mhsrc=ibmsearch_a&mhq=%E4%B8%8A%E4%B8%8B%E6%96%87%20Python](https://www.ibm.com/developerworks/cn/opensource/os-cn-pythonwith/index.html?mhsrc=ibmsearch_a&mhq=上下文 Python))

