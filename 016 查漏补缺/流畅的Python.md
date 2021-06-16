## 第一部分 序幕

### 第 1 章 Python 数据类型

1.4 为什么 len 不是普通方法

## 第二部分 数据结构

### 第 2 章 序列构成的数组

你们可能注意到了，之前提到的几个操作可以无差别地应用于文本、列表和表格上。我们把文本、列表和表格叫做数据火车…FOR 命令通常能作用于数据火车上。

ABC 语言是一个致力于为初学者设计编程环境的长达10年的研究项目，其中很多点子在现在看来都很有 Python 风格：序列的范型操作、内置的元组和映射类型、用缩进来架构的源码、无需变量声明的强类型等等。Python 对开发者如此友好，根源就在这里。

Python 也从 ABC 那里继承了用统一的风格去处理序列数据这一特点。不管是哪种数据结构，字符串、列表、字节序列、数组、XML 元素，抑或是数据库查询结果，它们都共用一套丰富的操作：迭代、切片、排序还有拼接。

深入理解 Python 中不同序列类型，不但能让我们避免重新发明轮子，它们的 API 还能帮助我们把我们自己定义的 API 设计的跟原生序列一样，或者是跟未来可能出现的序列类型保持兼容。

本章讨论的内容几乎可以应用到所有的序列类型上，从我们熟悉的 list, 到 Python3 中特有的 str 和 bytes。还会特别提到跟列表、元组、数组以及队列有关的话题。但是 Unicode 字符串和字节序列的内容被放在了第4章。另外这里讨论的数据结构都是 Python 中现成可用的，如果你想知道怎样创建自己的序列类型要等到第10章。

#### 2.1 内置序列类型概览



#### 2.2 列表推导和生成器表达式



##### 2.2.1 列表推导的可读性



##### 2.2.2 列表推导同 filter 和 map 的比较



##### 2.2.3 笛卡尔积



##### 2.2.4 生成器表达式



#### 2.3 元组不仅仅是不可变的列表

2.3.1 元组和激素

2.3.2 元组拆包

2.3.3 嵌套元组拆包

2.3.4 具名元组

2.3.5 作为不可变列表的元组

2.4 切片

2.4.1 为什么切片和区间会忽略最后一个元素

2.4.2 对对象进行切片

2.4.3 多位切片和省略

2.4.4 给切片复制

2.5 对序列使用+和*

2.6 序列的增量赋值

2.7 list.sort 方法和内置函数 sorted

2.8 用 bisect 来管理已排序的序列

2.8.1 用 bisect 来搜索

2.8.2 用 bisect.insort 插入新元素

2.9 当列表不是首选时

2.9.1 数组

2.9.2 内存时图

2.9.3 NumPy 和 SciPy

2.9.4 双向队列和其他形式的队列

2.10 本章小结

2.11 延伸阅读

### 第 3 章 字典和集合

### 第 4 章 文本和字节序列



## 第三部分 把函数视作对象

### 第 5 章 一等函数

> 不管别人怎么说或怎么想，我从未觉得 Python 受到来自函数式语言的太多影响。我非常熟悉命令式语言[^1]，如 C 和 Algol 68，虽然我把函数定为一等对象，但是我并不把 Python 当做函数式编程语言。
>
> ​	— 摘录自 Guido 的 The History of Python 博客，“[Origins of Python’s Functional Features](http://python-history.blogspot.jp/2009/04/origins-of-pythons-functional-features.html)”

在 Python 中，函数是一等对象。编程语言理论家把“一等对象”定义为满足下述条件的程序实体：

* 在运行时创建
* 能赋值给变量或数据结构中的元素
* 能作为参数传递给函数
* 能作为函数的返回结果

在 Python 中，整数、字符串和字典都是一等对象—没什么特别的。如果在 Python 之前，你使用的语言并未把函数当做一等公民，那么本章以及第三部分余下的内容将重点讨论把函数作为对象的影响和实际应用。

> 人们经常将“把函数视作一等对象”简称为“一等函数”。这样说并不完美，似乎表明这是函数中的特殊群体。在 Python 中，所有函数都是一等对象。

#### 5.1 把函数视作对象

示例 5-1 中的控制台会话表明，Python 函数是对象。这里我们创建了一个函数，然后调用它，读取它的`__doc__`属性，并且确认函数对象本身是 function 类的实例。



#### 5.2 高阶函数 map、filter和 reduce 的现代替代品

接受函数为参数，或者把函数作为结果返回的函数是高阶函数（higher-order function）。map 函数就是一例，如示例 5-2 所示。此外，内置函数 sorted 也是：可选的 key 参数用于提供一个函数，它会应用到各个元素上进行排序，参见 2.7 节。

例如，若想根据单词的长度排序，只需把 len 函数传给 key 参数，如示例 5-3 所示。



##### map、filter 和 reduce 的现代替代品

函数式语言通常会提供 map、filter 和 reduce 三个高阶函数（有时使用不同的名称）。在 Python 3 中，map 和 filter 还是内置函数，但是由于引入了列表推导式和生成器表达式，它们变得没那么重要了。列表推导式和生成器表达式具有 map 和 filter 两个函数的功能，而且更易于阅读，如示例 5-5 所示。

示例 5-5  计算阶乘列表： map 和 filter 与列表推导比较

```python
>>> list(map(fact, range(6)))
[1, 1, 2, 6, 24, 120]
>>> [fact(n) for n in range(6)]
[1, 1, 2, 6, 24, 120]
>>> list(map(factorial, filter(lambda n: n % 2, range(6))))
[1, 6, 120]
>>> [factorial(n) for n in range(6) if n % 2]
[1, 6, 120]
>>> [factorial(n) for n in range(6) if n % 2==0]
[1, 2, 24]
>>> [factorial(n) for n in range(6) if n % 2==1]
[1, 6, 120]
```

在 Python 3 中，map 和 filter 返回生成器（一种迭代器），因此现在他们的直接替代品是生成器表达式（在 Python 2 中，这两个函数返回列表，因此最接近的替代品是列表推导）。

在 Python 2 中，reduce 是内置函数，但是在 Python 3 中放到了 functools 模块里了。这个函数最常用于求和，自 2003 年发布的 Python 2.3 开始，最好使用内置的 sum 函数。在可读性和性能方面，这是一项重大改善。

示例 5-6 使用 reduce 和 sum 计算 0~99 之和

```python
In [14]: from functools import reduce
In [15]: from operator import add
In [16]: reduce(add, range(100))
Out[16]: 4950
In [17]: sum(range(100))
Out[17]: 4950
```

sum 和 reduce 的通用思想是把某个操作连续应用到序列的元素上，累计之前的结果，把一系列值归约成一个值。

all 和 any 也是内置的guiyue

#### 5.3 匿名函数



#### 5.4 可调用对象

5.5 用户定义的可调用类型

5.6 函数内省

5.7 从定位参数到仅限关键字参数

5.8 获取关于参数的信息

5.9 函数注解

5.10 支持函数式编程的包

5.10.1 operator 模块

5.10.2 使用 functools.partial 冻结参数

5.11 本章小结

5.12 延伸阅读

### 第 6 章 使用一等函数实现设计模式



### 第 7 章 函数装饰器和闭包

有很多人抱怨，把这个特性命名为“装饰器”不好。主要原因是，这个名称与 GoF 书[^7-1]使用的不一致。装饰器这个名称可能更适合在编译器领域使用，因为它会遍历并注解语法树。

​																	    —“PEP 318 — Decorators for functions and Methods”

函数装饰器用于在源码中“标记”函数，以某种方式增强函数的行为。这是一项强大的功能，但是若想掌握，必须理解闭包。

nonlocal 是新近出现的保留关键字，在 Python 3.0 中引入。作为 Python 程序员，如果严格遵守基于类的面向对象编程方式，即便不知道这个关键字也不会受到影响。然而，如果你想自己实现函数装饰器，那就必须了解闭包的方方面面，因此也就需要知道 nonlocal。

除了在装饰器中有用处之外，闭包还是回调式异步编程和函数式编程风格的基础。

本章的最终目标是解释清楚函数装饰器的工作原理，包括最简单的注册装饰器和较复杂的参数化装饰器。但是，在实现这一目标之前，我们要讨论下述话题：

* Python 是如何计算装饰器句法
* Python 如何判断变量是不是局部的
* 闭包存在的原因和工作原理
* nonlocal 能解决什么问题

掌握这些基础知识后，我们可以进一步探讨装饰器：

* 实现行为良好的装饰器
* 标准库中有用的装饰器
* 实现一个参数化装饰器

下面将首先介绍装饰器的基础知识，然后再讨论上面列出的各个话题。

#### 7.1 装饰器基础知识

装饰器是可调用的对象，其参数是另一个函数（被装饰的函数）。[^7-2] 装饰器可能会处理被装饰的函数，然后把它返回，或者将其替换成另一个函数或可调用对象。

假如有个名为 decorate 的装饰器：

```python
@decorate
def target():
    print('running target()')
```

上述代码的效果与下述写法一样：

```python
def target():
    print('running target()')
    
target = decorate(target)
```

两种写法的最终结果一样：上述两个代码片段执行完毕后得到的 target 不一定是原来那个 target 函数，而是 decorate(target) 返回的函数。

为了确认被装饰的函数会被替换，请看示例 7-1 中的控制台会话。

示例 7-1 装饰器通常把函数替换成另一个函数

```python
In [6]: def deco(func):
   ...:     def inner():
   ...:         print('running inner()')
   ...:     return inner	# deco 返回 inner 函数对象
   ...:

In [7]: @deco
   ...: def target():		# 使用 deco 装饰 target
   ...:     print('running target()')
   ...:

In [8]: target()		# 调用被装饰的 target 其实会运行 inner
running inner()

In [9]: target		# 审查对象，发现 target 现在是 inner 的引用
Out[9]: <function __main__.deco.<locals>.inner()>
```

严格来说，装饰器只是语法糖。如前所示，装饰器可以像常规的可调用对象那样调用，其参数是另一个函数。有时，这样做更方便，尤其是做元编程（在运行时改变程序的行为）时。

综上，装饰器的一大特性是，能把被装饰的函数替换成其他函数。第二个特性是，装饰器在加载模块时立即执行，下一节会说明。

#### 7.2 Python 何时执行装饰器

装饰器的一个关键特性是，它们在被装饰的函数定义之后立即运行。这通常是在导入时（即 Python 加载模块时）。如示例 7-2 中的 registration.py 模块所示。

示例 7-2 registration.py 模块

```python
```

注意，register 在模块中其他函数之前运行（两次）。调用 register 时，传给它的参数是被装饰的函数，例如 <function f1 at  0x0000000005DD21F0>。

加载模块后，registry 中有两个被装饰函数的引用：f1 和 f2。这两个函数，以及 f3，只在 main 明确调用它们时才执行。

如果导入 registration.py 模块，不作为脚本运行，输出如下：

```python
>>> import registration

```

此时查看 registry 的值，得到的输出如下：

```python
>>> registration.registry
```

示例 7-2 主要想强调，函数装饰器在导入模块时立即执行，而被装饰的函数只在明确调用时运行。这突出了 Python 程序员所说的导入时和运行时之间的区别。



7.3 使用装饰器改进“策略”模式

7.4 变量作用域规则

7.5 闭包

7.6 nonlocal 声明

7.7 实现一个简单的装饰器

7.8 标准库中的装饰器

7.8.1 使用 functools.lru_cache 做备忘

7.8.2 单分派泛函数

7.9 叠放装饰器

7.10 参数化装饰器

7.10.1 一个参数化的注册装饰器

7.10.2 参数化 clock 装饰器

7.11 本章小结

7.12 延伸阅读

## 第四部分 面向对象惯用法

### 第 8 章 对象引用、可变性和垃圾回收

8.1 变量不是盒子



### 第 9 章 符合 Python 风格的对象

#### 9.4 classmethod 与 staticmethod

Python 教程没有提到 classmethod 装饰器，也没有提到 staticmethod. 学过 Java 面向对象编程的人可能觉得奇怪，为什么 Python 提供两个这样的装饰器，而不是提供一个？

先来看 classmethod。示例 9-3 展示了它的用法：定义操作类，而不是操作实例的方法。classmethod 改变了调用方法的方式，因此类方法的第一个参数是类本身，而不是实例。classmethod 最常见的用途是定义备选构造方法，例如示例 9-3 中的 frombytes。注意，frombytes 的最后一行使用 cls 参数构建了一个新实例，即 cls(*memv). 按照约定，类方法的第一个参数名为 cls (但是 Python 不介意具体怎么命名)。

staticmethod 装饰器也会改变方法的调用方式，但是第一个参数不是特殊的值。其实，静态方法就是普通的函数，只是碰巧在类的定义体中，而不是在模块层定义。示例 9-4 对 classmethod 和 staticmethod 的行为做了对比：

示例 9-4 比较 classmethod 和 staticmethod 的行为

```python
In [5]: class Demo:
   ...:     @classmethod
   ...:     def klassmeth(*args):		# klassmeth 返回全部位置参数
   ...:         return args
   ...:     @staticmethod			
   ...:     def statmeth(*args):		# statmeth 也是返回全部位置参数
   ...:         return args
   ...:

In [6]: Demo.klassmeth()		# 不管怎样调用 Demo.klassmeth，它的第一个参数始终是 Demo 类
Out[6]: (__main__.Demo,)

In [7]: Demo.klassmeth('spam')
Out[7]: (__main__.Demo, 'spam')

In [8]: Demo.statmeth()			# Demo.statmeth 的行为与普通的函数相似
Out[8]: ()

In [9]: Demo.statmeth('spam')
Out[9]: ('spam',)
```

classmethod 装饰器非常有用，但我从未见过不得不用 staticmethod 的情况。如果想定义不需要与类交互的函数，那么在模块中定义就好了。有时，函数虽然从不处理类，但是函数的功能与类紧密相关，因此想把它放在近处。即便如此，在同一模块中的类前面或后面定义函数也就行了。[^5]

现在，我们对 classmethod 的作用已经有所了解（而且知道 staticmethod 不是特别有用），下面继续讨论对象的表示形式，说明如何支持格式化输出。

### 第 10 章 序列的修改、散列和切片





## 第六部分 元编程

### 第 19 章 动态属性和特性

#### 19.1 使用动态属性转换数据



#### 19.2 使用特性验证属性

目前，我们只介绍了如何使用 @property 装饰器实现只读属性。本节要创建一个可读写的特性。

##### 19.2.1 LineItem 类第1版：表示订单中商品的类

假设有个销售散装有机食物的电商应用，客户可以按重量订购坚果、干果或杂粮。在这个系统中，每个订单中都有一系列商品，而每个商品都可以使用示例 19-15 中的类表示。

示例 19-15 bulkfood_v1：最简单的 LineItem 类

```python
class LineItem:
    
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price
        
    def subtotal(self):
        return self.weight * self.price
```

这个类很精简，不过或许太简单了。示例 19-16 揭示了一个问题

示例 19-16 重量为负值时，金额小计为负值

```python
>>> raisins = LineItem('Golden raisins', 10, 6.95)
>>> raisins.subtotal()
69.5
>>> raisins.weight = -20	# 无效输入
>>> raisins.subtotal()		# 无效输出
-139.0
```

这个示例像玩具一样，但是没有想象中的那么好玩。下面是亚马逊早期的真实故事。我们发现顾客买书时可以把数量设为负数！然后，我们把金额打到顾客的信用卡上，苦苦等待他们把书寄出。[^12]

这个问题怎么解决呢？我们可以修改 LineItem 类的接口，使用读值方法和设值方法管理 weight 属性。这是 Java 采用的方式，这里也完全可行。

但是，如果能直接设定商品的 weight 属性，显得更自然。此外，系统可能在生产环境中，而其他部分已经直接访问 item.weight 了。此时，符合 Python 风格的做法是，把数据属性换成特性。（原文：In this case, the Python way would be to replace the data attribute with a property.）

##### 19.2.2 LineItem 类第2版：能验证值的特性

实现特性之后，我们可以使用读值方法和设值方法，但是 LineItem 类的接口保持不变（即，设值 LineItem 对象的 weight 属性依然写成 raisins.weight = 12）.

示例 19-17 列出可读写的 weight 特性的代码。

示例 19-17 bulkfood_v2.py：定义了 weight 特性的 LineItem 类

```python
In [12]: class LineItem:
    ...:     def __init__(self, description, weight, price):
    ...:         self.description = description
        		 # 这里已经使用特性的设值方法了，确保所创建实例的 weight 属性不能为负值
    ...:         self.weight = weight
    ...:         self.price = price
    ...:     def subtotal(self):
    ...:         return self.weight * self.price
    
    ...:     @property		# @property 装饰读值方法
    ...:     def weight(self):	# 实现特性的方法，其名称都与公开属性的名称一样--weight
    ...:         return self.__weight	# 真正的值存储在私有属性 __weight 中
    		 
        	 # 被装饰的读值方法有个.setter属性，这个属性也是装饰器；
             # 这个装饰器把读值方法和设值方法绑定在一起
    ...:     @weight.setter
    ...:     def weight(self, value):
    ...:         if value > 0:
    ...:             self.__weight = value	# 如果值大于零，设置私有属性 __weight
    ...:         else:
    ...:             raise ValueError('value must be > 0')	# 否则跑出 ValueError 异常
```

注意，现在不能创建重量为无效值的 LineItem 对象：

```python
In [13]: walnus = LineItem('walnuts', 0, 10.00)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-13-53e482623b05> in <module>
----> 1 walnus = LineItem('walnuts', 0, 10.00)

<ipython-input-12-089ce8068711> in __init__(self, description, weight, price)
      2     def __init__(self, description, weight, price):
      3         self.description = description
----> 4         self.weight = weight
      5         self.price = price
      6     def subtotal(self):

<ipython-input-12-089ce8068711> in weight(self, value)
     14             self.__weight = value
     15         else:
---> 16             raise ValueError('value must be > 0')
     17

ValueError: value must be > 0
```

现在，我们禁止用户为 weight 属性提供负值或零。虽然买家通常不能设置商品的价格，但是工作人员可能犯错，应用程序也可能有缺陷，从而导致 LineItem 对象的 price 属性为负值。为了防止出现这种情况，我们也可以把 price 属性变成特性，但是这样我们的代码中就存在一些重复。

Paul Graham 在第 14 章说过：当我在自己的程序中发现用到了模式，我觉得这就表明某个地方出错了。去除重复的方法是抽象。抽象特性的定义有两种方式：使用特性工厂函数，或者使用描述符类。后者更灵活，第 20 章会全面讨论。其实，特性本身就是使用描述符类实现的。不过，这里我们要继续探讨特性，实现一个特性工厂函数。

但是，在实现特性工厂函数之前，我们要深入理解特性。

#### 19.3 特性全解析

虽然内置的 property 经常用作装饰器，但它其实是一个类。在 Python 中，函数和类通常可以互换，因为二者都是可调用的对象，而且没有实例化对象的 new 运算符，所以调用构造方法与调用工厂函数没有区别。此外，只要能返回新的可调用对象，代替被装饰的函数，二者都可以用作装饰器。

property 构造方法的完整签名如下：

```python
property(fget=None, fset=None, fdel=None, doc=None)
```

所有参数都是可选的，如果没有把函数传给某个参数，那么得到的特性对象就不允许执行相应的操作。

property 类型在 Python 2.2 中引入，但是直到 Python 2.4 才出现 @ 装饰器句法，因此有那么几年，若想定义特性，则只能把存取函数传给前两个参数。

不使用装饰器定义特性的“经典”句法如示例 19-18 所示。

示例 19-18 bulkfood_v2b.py：效果与示例 19-17 一样，只不过没使用装饰器

```python
class LineItem:
    
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price
        
    def subtotal(self):
        return self.weight * self.price
    
    def get_weight(self):		# 普通的读值方法
        return self.__weight
    
    def set_weight(self, value):	# 普通的设值方法
        if value > 0:
            self.__weight = value
        else:
            raise ValueError('value must be > 0')
    
    # 构建 property 对象，然后赋值给公开的类属性
    weight = property(get_weight, set_weight)
```

某些情况下，这种经典形式比装饰器句法好；稍后讨论的特性工厂函数就是一例。但是，在方法众多的类定义体中使用装饰器的话，一眼就能看出哪些是读值方法，哪些是设值方法，而不用按照惯例，在方法名前面加上 get 和 set。

类中的特性能影响示例属性的寻找方式，而一开始这种方式可能会让人觉得意外。

##### 19.3.1 特性会覆盖实例属性

特性都是类属性，但是特性管理的其实是实例属性的存取。

9.9 节说过，如果实例和所属的类有同名数据属性，那么实例属性会覆盖（或称遮盖）类属性 — 至少通过那个实例读取属性时是这样。示例 19-19 阐明了这一点。

示例 19-19 实例属性遮盖类的数据属性。

```python
In [15]: class Class:	# 定义 Class 类，这个类有两个类属性：data 数据属性和 prop 特性
    ...:     data = 'the class data attr'
    ...:     @property
    ...:     def prop(self):
    ...:         return 'the prop value'
    ...:

In [16]: obj = Class()

In [17]: vars(obj)	# vars 函数返回 obj 的__dict__属性，表明没有实例属性
Out[17]: {}

In [18]: obj.data	# 读取 obj.data,获取的是 Class.data 的值
Out[18]: 'the class data attr'

In [19]: obj.data = 'bar'	# 为 obj.data 赋值，创建一个实例属性

In [20]: vars(obj)	# 审查实例，查看实例属性
Out[20]: {'data': 'bar'}

In [21]: obj.data	# 现在读取 obj.data，获取的是实例属性的值。从 obj 实例中读取属性时，实例属性 						# data会遮盖类属性 data
Out[21]: 'bar'

In [22]: Class.data	# Class.data 属性的值完好无损
Out[22]: 'the class data attr'
```

下面尝试覆盖 obj 实例的 prop 特性。接着前面控制台会话，输入示例 19-20 中的代码。

示例 19-20 实例属性不会遮盖类属性（接续示例 19-19）

```python
In [23]: Class.prop
Out[23]: <property at 0x10f4da3b0>

In [24]: obj.prop
Out[24]: 'the prop value'

In [25]: obj.prop = 'foo'
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-25-950b619b2a59> in <module>
----> 1 obj.prop = 'foo'

AttributeError: can't set attribute

In [26]: obj.__dict__['prop'] = 'foo'

In [27]: vars(obj)
Out[27]: {'data': 'bar', 'prop': 'foo'}

In [28]: obj.prop
Out[28]: 'the prop value'

In [29]: Class.prop = 'baz'

In [30]: obj.prop
Out[30]: 'foo'
```

示例 19-21 新添的类特性遮盖现有的实例属性（接续示例 19-20）

```python
In [31]: obj.data
Out[31]: 'bar'

In [32]: Class.data
Out[32]: 'the class data attr'

In [33]: Class.data = property(lambda self: 'the "data" prop value')

In [34]: obj.data
Out[34]: 'the "data" prop value'

In [35]: del Class.data

In [36]: obj.data
Out[36]: 'bar'
```

本节的主要观点是，obj.attr 这样的表达式不会从 obj 开始寻找 attr，而是从 `obj.__class__`开始，而且，仅当类中没有名为 attr 的特性时，Python 才会在 obj 实例中寻找。这条规则不仅适用于特性，还适用于一整类描述符 — 覆盖型描述符（overriding descriptor）。第 20 章会进一步讨论描述符，那时你会发现，特性其实是覆盖型描述符。

现在回到特性。各种 Python 代码单元（模块、函数、类和方法）都可以有文档字符串。下一节说明如何把文档依附到特性上。

##### 19.3.2 特性的文档

#### 19.4 定义一个特性工厂函数



#### 19.5 处理属性删除操作

















[^7-1]: 指 1995 年出版的英文原版《设计模式：可复用面向对象软件的基础》，作者是四个人，人们称之为“四人组”（Gang of Four)
[^7-2]: Python 也支持类装饰器，参见第 21 章
[^5]: 本书的技术审校之一 Leonardo Rochael 不同意我对 staticmethod 的见解，作为反驳，他推荐阅读 Julien Danjou 写的一篇博客文章，题为“[The Definitive Guide on How to Use Static, Class or Abstract Methods in Python](https://julien.danjou.info/guide-python-static-class-abstract-methods/)”. Danjou 的这篇文章写的很好，但是我对 staticmethod 的观点依然不变，请读者自辨。
[^12]: 摘自华尔街日报的文章，“[Birth of a Salesman](https://www.wsj.com/articles/SB10001424052970203914304576627102996831200)”(2011 年 10 月 15 日)，这是 Jeff Bezos 的原话。

 















