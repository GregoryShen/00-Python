## 第一章 数据结构和算法

## 第二章 字符串和文本

第三章 数字日期和时间

第四章 迭代器和生成器

第五章 文件与 IO

第六章 数据编码和处理

## 第七章 函数

使用 def 语句定义函数是所有程序的基础。本章的目标是讲解一些更高级和不常见的函数定义与使用模式。涉及到的内容包括默认参数、任意数量参数、强制关键字参数、强制关键字参数、注解和闭包。另外，一些高级的控制流和利用回调函数传递数据的技术在这里也会讲解到。

### 7.1 可接受任意数量参数的函数

#### 问题

你想构造一个可接受任意数量参数的函数。

#### 解决方案

为了能让一个函数接受任意数量的位置参数，可以使用一个*参数，例如：

```python
In [38]: def avg(first, *rest):
    ...:     return (first + sum(rest)) / (1 + len(rest))
    ...:

# Sample use
In [39]: avg(1, 2)
Out[39]: 1.5

In [40]: avg(1, 2, 3, 4)
Out[40]: 2.5
```

在这个例子中，rest 是由所有其他位置参数组成的元组。然后我们在代码中把它当成了一个序列来进行后续的计算。

为了接受任意数量的关键字参数，使用一个`**`开头的参数。比如：

```python
In [42]: import html

In [43]: def make_element(name, value, **attrs):
    ...:     keyvals = [' %s="%s"' % item for item in attrs.items()]
    ...:     attr_str = ''.join(keyvals)
    ...:     element = '<{name}{attrs}>{value}</{name}>'.format(
    ...:             name=name,
    ...:             attrs=attr_str,
    ...:             value=html.escape(value))
    ...:     return element
    ...:

In [44]: make_element('item', 'Albatross', size='large', quantity=6)
Out[44]: '<item size="large" quantity="6">Albatross</item>'

In [45]: make_element('p', '<spam>')
Out[45]: '<p>&lt;spam&gt;</p>'
```

在这里， attrs 是一个包含所有被传入进来的关键字参数的字典。

如果你还希望某个函数能同时接受任意数量的位置参数和关键字参数，可以同时使用`*`和`**`，比如：

```python
In [46]: def anyargs(*args, **kwargs):
    ...:     print(args)	# A tuple
    ...:     print(kwargs)	# A dict
```

使用这个函数时，所有的位置参数会被放到 args 元组中，所有关键字参数会被放到字典 kwargs 中。

#### 讨论

一个`*`参数只能出现在函数定义中最后一个位置参数后面，而`**`参数只能出现在最后一个参数。有一点要注意的是，在`*`参数后面仍然可以定义其他参数。

```python
def a(x, *args, y):
    pass

def b(x, *args, y, **kwargs):
    pass
```

这种参数就是我们所说的强制关键字参数，在后面 7.2 小节还会详细讲解到。

7.2 只接受关键字参数的函数

7.3 给函数参数增加元信息

7.4 返回多个值的函数

7.5 定义有默认参数的函数

7.6 定义匿名或内联函数

7.7 匿名函数捕获变量值

7.8 减少可调用对象的参数个数

7.9 将单方法的类转换为函数

7.10 带额外状态信息的回调函数

7.11 内联回调函数

7.12 访问闭包中定义的变量



第八章 类与对象

第九章 元编程

第十章 模块与包

第十一章 网络与 Web 编程

第十二章 并发编程

第十三章 脚本编程与系统管理

第十四章 测试、调试和异常

第十五章 C 语言扩展

## 第九章 元编程

软件开发领域中最经典的口头禅就是“don’t repeat yourself”。也就是说，任何时候当你的程序中存在高度重复（或者是通过剪切复制）的代码时，都应该想想是否有更好的解决方案。在 Python 中，通常都可以通过元编程来解决这类问题。简言之，元编程就是关于创建操作源代码（比如修改、生成或包装原来的代码）的函数和类。主要技术是使用装饰器、类装饰器和元类。不过还有一些其他技术，包括签名对象、使用`exec()`执行代码以及对内部函数和类的反射技术等。本章的主要目的是向大家介绍这些元编程技术，并且给出实例来演示他们是怎样定制化你的源代码行为的。

> ### [Python元编程：控制你想控制的一切](https://zhuanlan.zhihu.com/p/29849145)
>
> 很多人不理解“元编程”是个什么东西，关于它也没有一个十分准确的定义。这篇文章要说的是 Python 里的元编程，实际上也不一定就真的符合“元编程”的定义。只不过我无法找到一个更准确的名字来代表这篇文章的主题，所以就借了这么一个名号。
>
> 副标题是控制你想控制的一切。实际上这篇文章讲的都是一个东西，利用 Python 提供给我们的特性，尽可能的使代码优雅简洁。具体而言，通过编程的方法，在更高的抽象层次上对一种层次的抽象的特性进行修改。
>
> 首先说，Python 中一切皆对象，还有，Python 提供了许多特殊方法、元类等等这样的“元编程”机制。像给对象动态添加属性方法之类的，在 Python 中根本谈不上是“元编程”，但在某些静态语言中却是需要一定技巧的东西。我们来谈些 Python 程序员也容易被搞糊涂的东西。
>
> 我们先来把对象分分层次，通常我们知道一个对象有它的类型，老早以前 Python 就将类型也实现为对象。这样我们就有了实例对象和类对象。这是两个层次。稍有基础的读者就会知道还有元类这个东西的存在，简言之，元类就是类的类，也就是比类更高层次的东西。这又有了一个层次。
>
> #### ImportTime vs. RunTime
>
> 如果我们换个角度，不用非得和之前的三个层次使用同样的标准。我们再来区分两个东西：ImportTime 和 RunTime，它们之间也非界限分明，顾名思义，就是两个时刻，导入时和运行时。
>
> 当一个模块被导入时，会发生什么？在全局作用域的语句（非定义性语句）被执行。函数定义：一个函数对象被创建，但其中的代码不会被执行。类定义：一个类对象被创建，类定义域的代码被执行，类的方法中的代码自然也不会被执行。
>
> 执行时：函数和方法中的代码会被执行，当然你要先调用它们。
>
> #### 元类
>
> #### 装饰器
>
> #### 对数据的抽象-描述符
>
> #### 控制子类的创建-代替元类的方法
>
> #### 小结
>
> 诸如元类等元编程对于大多数人来说有些晦涩难懂，大多数时候也无需用到它们。但是大多数框架背后的实现都使用到了这些技巧，这样才能让使用者写出来的代码简洁易懂。如果你想更深入的了解这些技巧，可以参看一些书籍例如《Fluent Python》、《Python Cookbook》，或者看官方文档中的某些章节例如上文说的描述符HowTo，还有Data Model 一节等等。或者直接看 Python 的源码，包括用 Python 写的以及 CPython 的源码。
>
> 记住，只有在充分理解了它们之后再去使用，也不要是个地方就想着使用这些技巧。

### 9.1 在函数上添加包装器

#### 问题

你想在函数上添加一个包装器，增加额外的操作处理（比如日志、计时等）

#### 解决方案

如果你想使用额外的代码包装一个函数，可以定义一个装饰器函数，例如：

```python
```



#### 讨论



### 9.2 创建装饰器时保留函数元信息

#### 问题

你写了一个装饰器作用在某个函数上，但是这个函数的重要元信息比如名字、文档字符串、注解和参数签名都丢失了。

#### 解决方案

任何时候你定义装饰器的时候，都应该使用 functools 库中的 @wraps 装饰器来注解底层包装函数。例如：

```python
In [1]: import time
In [2]: from functools import wraps
In [3]: def timethis(func):
   ...:     '''
   ...:     Decorator that reports the execution time.
   ...:     '''
   ...:     @wraps(func)
   ...:     def wrapper(*args, **kwargs):
   ...:         start = time.time()
   ...:         result = func(*args, **kwargs)
   ...:         end = time.time()
   ...:         print(func.__name__, end-start)
   ...:         return result
   ...:     return wrapper
```

下面我们使用这个被包装后的函数并检查它的元信息：

```python
In [4]: @timethis
   ...: def countdown(n):
   ...:     '''
   ...:     Counts down
   ...:     '''
   ...:     while n > 0:
   ...:         n -= 1
   ...:
In [5]: countdown(10000)
countdown 0.0009999275207519531
In [6]: countdown.__name__
Out[6]: 'countdown'
In [7]: countdown.__doc__
Out[7]: '\n    Counts down\n    '
In [9]: countdown.__annotations__
Out[9]: {}
```

#### 讨论

在编写装饰器的时候复制元信息是一个非常重要的部分。如果你忘记了使用@wraps，那么你会发现被装饰函数丢失了所有有用的信息。比如如果忽略@wraps后的效果是下面这样的：

```python
>>> countdown.__name__
'wrapper'
>>> countdown.__doc__
>>> countdown.__annotations__
{}
>>>
```

@wraps 有一个重要特征是它能让你通过属性`__wrapped__`直接访问被包装函数。例如：

```python
In [10]: countdown.__wrapped__(1000000)
```

`__wrapped__` 属性还能让被装饰函数正确暴露底层的参数签名信息。例如：

```python
In [11]: from inspect import signature
In [12]: print(signature(countdown))
(n)
```

一个很普遍的问题是怎样让装饰器去直接复制原始函数的参数签名信息，如果想自己动手实现的话需要做大量的工作，最好就简单地使用@wraps 装饰器。通过底层的`__wrapped__`属性访问到函数签名信息。

### 9.3 解除一个装饰器

#### 问题

#### 解决方案

#### 讨论

### 9.4 定义一个带参数的装饰器

#### 问题



#### 解决方案



#### 讨论



### 9.5 可自定义属性的装饰器

#### 问题

你想写一个装饰器来包装一个函数，并且允许用户提供参数在运行时控制装饰器行为。

#### 解决方案

引入一个访问函数，使用 nonlocal 来修改内部变量。然后这个访问函数被作为一个属性赋值给包装函数。

```python
In [14]: from functools import wraps, partial
In [15]: import logging

# utility decorator to attach a function as an attribute of obj
In [16]: def attach_wrapper(obj, func=None):
    ...:     if func is None:
    ...:         return partial(attach_wrapper, obj)
    ...:     setattr(obj, func.__name__, func)
    ...:     return func
    ...:

In [17]: def logged(level, name=None, message=None):
    ...:     '''
    ...:     Add logging to a function, level is the logging
    ...:     level, name is the logger name, and message is the
    ...:     log message. If name and message aren't specified,
    ...:     they defalt to the function's module and name.
    ...:     '''
    ...:     def decorate(func):
    ...:         logname = name if name else func.__module__
    ...:         log = logging.getLogger(logname)
    ...:         logmsg = message if message else func.__name__
        
    ...:         @wraps(func)
    ...:         def wrapper(*args, **kwargs):
    ...:             log.log(level, logmsg)
    ...:             return func(*args, **kwargs)
    			
        		 # Attach setter functions
    ...:         @attach_wrapper(wrapper)
    ...:         def set_level(newlevel):
    ...:             nonlocal level
    ...:             level = newlevel
        
    ...:         @attach_wrapper(wrapper)
    ...:         def set_message(newmsg):
    ...:             nonlocal logmsg
    ...:             logmsg = newmsg
    ...:         return wrapper
    ...:     return decorate
    ...:

# Example use
In [18]: @logged(logging.DEBUG)
    ...: def add(x, y):
    ...:     return x + y
    ...:

In [19]: @logged(logging.CRITICAL, 'example')
    ...: def spam():
    ...:     print('Spam!')
```

下面是交互环境下的使用例子：

```python
In [19]: import logging
In [20]: logging.basicConfig(level=logging.DEBUG)
In [21]: add(2, 3)
DEBUG:__main__:add
Out[21]: 5
# Change the log message
In [22]: add.set_message('Add called')
In [23]: add(2, 3)
DEBUG:__main__:Add called
Out[23]: 5
# Change the log level
In [25]: add.set_level(logging.WARNING)
In [26]: add(2, 3)
WARNING:__main__:Add called
Out[26]: 5
```

#### 讨论





