# Python 错误与异常

## 第1章 错误和异常概念

#### 课程大纲:

* 错误和异常概念
* 常见的错误
* 异常处理
  * `try_except`使用及`else`使用
  * 截获异常
  * `try_finally`使用
  * 异常处理综合使用
* `with…as`语句与上下文管理
* 标准异常和自定义异常
* `raise`和 `assert`语句

#### 错误和异常概念

错误:

1. 语法错误: 代码不符合解释器或者编译器语法
2. 逻辑错误: 不完整或者不合法输入或者计算出现问题

异常: 执行过程中出现问题导致程序无法执行

1. 程序遇到逻辑或者算法问题
2. 运行过程中计算机错误(内存不够或者IO错误)

#### 错误和异常区别

错误:

​		代码运行前的语法或者逻辑错误,语法错误在执行前修改,逻辑错误无法修改

异常分为两个步骤:

1. 异常产生, 检查到错误且解释器认为是一场,抛出异常
2. 异常处理,截获异常,忽略或者终止程序处理异常

## 第2章 错误和异常的处理方式

### 2-1 Python 常见错误

### 2-2 使用try…except处理

### 2-3 使用try…except处理异常

### 2-4 try_finally 使用

### 2-5 try-except-else

### 2-6 with…as语句

首先来认识下`with`语句,`with`语句的基本语法是这样的:

```python
with context [as var]:
    with_suite
```

关键字`with`,然后加一个context表达式,后面再加一个 `as var`(后面会有介绍),`with_suite`是`with`所执行的语句

1. `with`语句其实是用来代替`try...except...finally`语句的,它的作用是使代码更加简洁
2. `with`是一个关键字,而context表达式它返回的是一个对象,这个对象应该要支持上下文协议
3. `as var`是用来保存context返回的对象的,这个返回的对象可以是多个值也可以是一个值,多个值的话就是一个元组
4. `with_suite`就是使用`var`变量来对context返回的对象进行操作

当`with`执行的时候它会把context语句返回的对象赋值给`var`,然后在`with_suite`代码块中就会使用`var`变量对context返回的对象进行操作

我们来看一个`with`语句的实例:我们来看一下`with`语句对一个文件对象进行操作:

```python
with open('1.txt') as f:
    for line in f.readlines():
        print(line)
```

1. 我们最简单的格式就是打开一个文件—> `open(‘1.txt’)` ,这个表达式会返回一个文件对象.当返回文件对象后,临时的文件对象file就会被赋值给`f`变量.在后面的`with`语句中对文件的操作都是使用`f`来进行操作的
2. 那么`f`变量就会接收文件对象所返回的对象
3. `with`中的代码块执行完之后并没有显式地执行文件关闭的操作.当with中的代码块执行完成或with代码块中出现了错误或异常,首先要关闭文件,然后再去处理错误或异常.如果没有错误或异常发生,那么执行完成之后就会自动地把文件关闭.

下面来看两种方法的对比:

```python
try:
    f = open('1.txt')
    print("in try f.read()", f.read(2))
except IOError, e:
    print("catch IOError", e)
except ValueError, e:
    print("catch ValueError", e)
finally:
    f.close()
print("try-finally:", f.closed)


with open('1.txt') as f1:
    print("in with f1.read()", f1.read())
print("with :", f1.closed)
```

两种方法都会打印出文件的关闭状态(`f.closed`)

运行文件得到结果:

![截屏2020-02-1916.31.33](/Users/gregoryshen/截图/截屏2020-02-1916.31.33.png)

可以看到f1这个文件最后也是关闭的.

如果文件在打开或访问的过程中出现了IO错误,`try…except…finally`肯定也是会把文件关闭掉的,而`with`语句能否在出现IO错误的情况下保证文件也是关闭的呢?对此我们再做一个实验:

导入`os`模块,然后做一个`seek`的操作(我们读完文件肯定到尾了,这个时候`f.seek(-5, os.SEEK_SET)`在头的位置向前5个肯定是会报错的), 在`with`语句中同样也执行这样的操作:

```python
import os

try:
    f = open('1.txt')
    print("in try f.read()", f.read())
    f.seek(-5, os.SEEK_SET)
except IOError, e:
    print("Catch IOError: ", e)
except ValueError, e:
    print("Catch ValueError: ", e)
finally:
    f.close()
print("try-finally:", f.closed)


with open('1.txt') as f1:
    print('in with f1.read()', f1.read())
    f.seek(-5, os.SEEK_SET)
print("with:", f1.closed)
```

运行结果如下:

![截屏2020-02-1917.27.27](/Users/gregoryshen/截图/截屏2020-02-1917.27.27.png)

try语句正常,with语句也会出现这个错误,这个错误之后文件就没有被关闭掉,我们认为这种方式是有问题的.没有被关闭掉的原因是这里没有对`ValueError`做处理.

`with`语句没有对捕获的错误进行处理.`with`语句虽然说可以保证文件被关闭,但是当文件访问发生错误的时候,文件的错误异常并没有被真正地处理,这个会交给系统(也就是Python解释器)来处理,交给用户来处理.错误肯定还是要上报的.

把代码改一下,使用`try…except`语句来捕获`ValueError`,捕获的目的是说确认一下当我们出现错误的时候`with`语句它也是能够正常把文件关闭的.

```python
try:
  	with open('1.txt') as f1:
        print('in with f1.read()', f1.read())
        f.seek(-5, os.SEEK_SET)
except ValueError, e:
    print("in with catch ValueError:", e)
    print("with:", f1.closed)
```

运行程序得到结果:

![截屏2020-02-1918.08.39](/Users/gregoryshen/截图/截屏2020-02-1918.08.39.png)

这里我们捕捉到了错误,而当出现这个错误的的时候, 文件已经被关闭了.

再分析一下执行过程:

首先用`with`打开了`F.txt`,然后把它赋值给`f1`,使用`f1`读出了文件中的所有内容,然后执行`seek`操作,在`seek`操作的时候会发生`ValueError`的异常.

这个异常在抛出之前,`with`语句首先要把文件关闭掉,之后才把异常向上抛出,抛出之后`try`语句就会截获到`ValueError`,然后就会把文件的状态打印出来.

下面来分析下`with`语句是如何来对文件对象保证它执行完成或者中间出现异常的时候把它关闭掉的:

#### with语句实质

`with`语句的实质是上下文管理机制

**什么是上下文管理协议?**

​	  包含两个方法,一个是`__enter__`方法,另一个是`__exit__`方法,支持该协议的对象要实现这两个方法,才能被`with`语句进行操作

**上下文管理器**

​	  当定义执行`with`语句时需要建立一个运*<u>行时上下文</u>*,它就负责执行`with`语句块中上下文中的进入与退出操作

**什么时候进入/退出?**

​	  当进入上下文的时候,我们需要调用管理器的`__enter__`方法,调用`context`表达式返回的对象时,自动去调用这个对象的`__enter__`方法,这个`__enter__`方法应该会返回一个它本身的对象,如果说设置了`as var`语句,`var`变量就会接受`__enter__`方法的返回值.

然后会使用`var`在`with`代码块中进行操作,当代码执行完成或者代码执行过程中出现了异常,退出的时候,上下文管理器就会调用管理器的`__exit__`方法,对资源进行清理,对文件进行关闭.

这就是`with`语句执行的过程和基本的原理.

既然我们明白了上下文管理协议,我们就自己实现一个类,来让它支持上下文管理协议,然后加一些打印信息,更好地了解`with`语句执行的实际过程:

```python
 class MyContext(object):
    
 		def __init__(self, name):
    		self.name = name
        
    def __enter__(self):
      	print("__enter__")
        return self
      
    def do_self(self):
      	print("do_self")
        
    def __exit__(self, exc_type, exc_value, traceback):
      	print("__exit__")
        print("Error:", exc_type, " info:", exc_value)
        

if __name__ == '__main__':
  	with MyContext('test context') as f:
      	print(f.name)
        f.do_self()
```

这里实现了一个`MyContext`类,这个类支持上下文协议(它实现了`__enter__`和`__exit__`方法).

在`__init__`方法中只是传进来了一个名字,`do_self`方法就是打印了一条do_self.

在`__enter__`方法中打印了一条\__enter__信息,然后返回了对象自己本身.

在`__exit__`方法中会有几个参数,`exc_type`就是错误的类型,`exc_value`错误类型的一些描述信息,`traceback`是出错的堆栈信息,我们可以根据堆栈信息确认代码是在哪一行出了错误.

在`main`函数中是使用`with`语句来对`MyContext`进行操作,我们主要的目的是看一下使用with进行操作的时候每一个函数具体的调用过程.

`with`代码段首先要打印出`f`的`name`,然后调用`do_self`方法.

运行代码查看具体调用过程:

![截屏2020-02-2000.57.02](/Users/gregoryshen/截图/截屏2020-02-2000.57.02.png)

 首先会调用`__enter__`方法,之后会把自己本身返回给我们一个`MyContext`对象,这个对象就会赋给后面的`f`;而`f`首先要打印出它的名字,确实是`MyContext`的对象.然后调用`do_self`方法,打印出do_self,这个时候代码就已经执行完成了,执行完成后就调用了`__exit__`方法,在`__exit__`方法中发现错误以及错误信息都是`None`.

这是正常的一个过程,我们再来看一个非正常的过程: 比如在do_self下加一个没有定义的变量`a`:这个时候在执行`do_self`的时候会出现一个异常.那我们来看一下是先出的异常还是先做`__exit__`退出操作.

执行一下代码:

![截屏2020-02-2100.47.50](/Users/gregoryshen/截图/截屏2020-02-2100.47.50.png)

首先前面的过程是不变的,但是在我们做`do_self`的时候,首先a肯定是一个错误因为名字没有被定义,所以这里发生异常以后首先调用`__exit__`方法,看到错误类型是`NameError`,错误信息是有个名字`a`没有定义,然后把`Traceback`也打印了出来,最后把这个异常抛给了Python解释器,由Python解释器来处理这个异常,这时代码就执行完成了.

从上面的执行过程中我们可以了解到,比如文件以及一些锁的机制也同样支持`__enter__`和`__exit__`方法.当我们对文件进行操作的时候,它首先也是进入`__enter__`方法,并把文件对象返回出来,之后这个对象是要赋给`var`变量的,然后使用`var`变量来对文件进行操作.当我们出现异常或`with`代码段执行完成之后,自动会调用`__exit__`方法对文件进行关闭操作,这个就是`with`语句正常的执行过程.

那我们来看下`with`语句的应用场景:

1. 文件操作
2. 进程线程之间互斥对象,例如互斥锁、信号量等等
3. 自定义的一些支持上下文的其他对象

## 第3章 标准异常和自定义异常

### 3-1 assert 和raise 语句

### 3-2 标准异常和自定义异常



