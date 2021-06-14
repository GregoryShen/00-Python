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

