# [廖雪峰：使用dict和set](https://www.liaoxuefeng.com/wiki/1016959663602400/1017104324028448)

Python内置了字典：dict的支持，dict全称dictionary， 在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度

给定一个名字，比如‘Michael’， dict在内部就可以直接计算出Michael对应的存放成绩的页码，也就是95这个数字存放的内存地址，直接取出来，所以速度非常快。

这种key-value存储方式，在放进去的时候，必须根据key算出value的存放位置，这样，取的时候才能根据key直接拿到value

把数据放入dict的方法，除了初始化时指定外，还可以通过key放入：

```python
>>> d['Adam'] = 67
>>> d['Adam']
67
```

由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉

如果key不存在，dict就会报错

要避免key不存在的错误，有两种办法，一是通过in判断key是否存在，而是通过dict提供的`get()`方法，如果key不存在，可以返回None， 或者自己指定的value（注意：返回None的时候Python的交互环境不显示结果）

要删除一个key，用`pop(key)`方法，对应的value也会从dict中删除（注意：dict内部存放的顺序和key放入的顺序是没有关系的）

和list比较，dict有以下几个特点：

1. 查找和插入的速度极快，不会随着key的增加而变慢
2. 需要占用大量的内存，内存浪费多

而list相反：

1. 查找和插入的时间随着元素的增加而增加
2. 占用空间小，浪费内存很少

所以，dict是用空间来换取时间的一种方法。

dict的key必须是不可变对象，因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法

要保证hash的正确性，作为key的对象就不能变。在Python中，字符串，整数等都是不可变的，而list是可以变的，就不能作为key

## set

set和dict类似，也是一组key的组合，但不存储value。由于key不能重复，所以，在set中，没有重复的key

要创建一个set，需要提供一个list作为输入集合

```python
>>> s = set([1, 2, 3])
>>> s
{1, 2, 3}
```

注意，传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3} 只是告诉你这个set内部有1， 2， 3这3个元素，显示的顺序也不表示set是有序的

重复元素在set中自动被过滤

通过`add(key)`方法可以添加元素到set中，可以重复添加，但不会有效果

通过`remove(key)`方法可以删除元素

set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集，并集等操作：

```python
>>> s1 = set([1, 2, 3])
>>> s2 = set([2, 3, 4])
>>> s1 & s2
[2, 3]
>>> s1 | s2
>>> [1, 2, 3, 4]
```

set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。

对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的

## [Python3 字典](https://www.runoob.com/python3/python3-dictionary.html)

字典是另一种可变容器模型，且可存储任意类型对象

字典的每个键值对用冒号分割，每对之间用逗号分割，整个字典包括在花括号中

键必须是唯一的，但值则不必

值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组

访问字典里的值：把相应的键放入到方括号中

修改字典：向字典添加新内容的方法是增加新的键/值对，修改或删除已有

删除字典元素：del dict[‘name’]  #删除键‘name’

dict.clear() 清空字典

del dict   删除字典

[Python dict() 函数](https://www.runoob.com/python/python-func-dict.html)

这个讲的还是很优秀的

`dict()`函数用于创建一个字典。

dict 语法：

```python
class dict(**kwargs)
class dict(mapping, **kwargs)
class dict(iterable, **kwargs)

# 参数说明:
# **kwargs 关键字
# mapping  元素的容器
# iterable 可迭代对象
```

实例：

```python
>>> dict()			# 创建空字典
{}
>>> dict(a='a', b='b', t='t')		# 传入关键字
{'a': 'a', 'b': 'b', 't': 't'}
>>> dict(zip(['one', 'two', 'three'], [1, 2, 3]))	# 映射函数方式来构造字典
{'three': 3, 'two': 2, 'one': 1} 
>>> dict([('one', 1), ('two', 2), ('three', 3)]) 	# 可迭代对象方式来构造字典
{'three': 3, 'two': 2, 'one': 1}
```

扩展： `zip` 函数

`zip()`函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存

可以使用`list()`转换来输出列表

如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用`*`操作符号，可以将元组解压为列表





[Python——字典dict()详解](https://www.cnblogs.com/mingmingming/p/11050495.html)

字典是python提供的一种数据类型，用于存放有映射关系的数据。字典相当于两组数据，其中一组是key，是关键数据（程序对字典的操作都是基于key），另一组数据是value，可以通过key来进行访问

> class dict(object)
>
> dict() -> new empty dictionary
>
> dict(mapping) -> new dictionary initialized from a mapping object’s (key, value) pairs
>
> dict(iterable) -> new dictionary initialized as if via:
>
> d = {}
>
> for k, v in iterable:
>
> d[k] = v
>
> dict(**kwargs) -> new dictionary initialized with the name=value pairs in the keyword argument list. For example: dict(one=1, two=2)

字典的常用方法：

1. `clear`
2. `copy`
3. `fromkeys`
4. `get`
5. items
6. keys
7. values

注意事项：

列表不允许对不存在的索引复制，但字典允许对不存在的键复制

```python
p = [1, 2, 3, 4, 5]
# 对不存在的索引赋值
p[5] = 666
# 报错 IndexError: list assignment index out of range

q = dict(a=1, b=2)
# 对不存在的key赋值
q['c'] = 3
print(q)


```



[python: dict(字典) 操作](https://blog.csdn.net/JNingWei/article/details/78757673)

key-value

|    名称     | 唯一性 |     数据类型     | 可变性 |
| :---------: | :----: | :--------------: | :----: |
|  key（键）  |  唯一  | 数字/字符串/元组 | 不可变 |
| value（值） | 不唯一 |       任意       |  可变  |

字典定义

字典访问

​	通过指定key值访问对应的value

字典长度

字典打印

​	以字符串形式

```python
dict = {'city': 'nanjing', 'university': 'NUAA'}

# 字典打印（以字符串形式）
assert str(dict) == "{'city': 'nanjing', 'university': 'NUAA'}"
```

字典复制：浅复制

字典取值：不修改字典：get方法

​					修改字典：

key存在： if i in dict

可遍历的key-value数组：`dict.items()`

key列表： `dict.keys()`

value列表： `dict.values()`

### 字典合并

通过`update`合并字典

```python
dict = {'city': 'nanjing', 'university': 'NUAA'}
dict_2 = {'collage': 'cs', 'degree': 'master'}

dict.update(dict_2)
assert dict == {'city': 'nanjing', 'university': 'NUAA', 'collage': 'cs', 'degree': 'master'}
```

注意：

如果合并时，存在相同的key值，那么只会保留后者的键值对，而非合并：

字典删除:

1. 通过`pop`

删除字典给定键key所对应的值,返回值为被删除的值.key值必须给出,否则返回default值



1. 通过`del`
2. 通过`popitem`



https://www.w3cschool.cn/python/python-dictionary.html

https://www.jianshu.com/p/f2c2f1d642a6

https://www.cnblogs.com/tkqasn/p/5977653.html



# [你知道和不知道的Python字典都在这里！！](https://mp.weixin.qq.com/s/36_gHzFKpQ9rIscFOfUboQ)

本文从6个方面介绍字典，包括：字典创建的5种方式、访问字典元素、字典元素添加、字典元素删除、字典的其他方法、序列解包（拆包）

## 字典

字典是“键值对”的无序可变序列，字典中的每个元素都是一个“键值对”，包含：“键对象”和“值对象”。可以通过“键对象”实现快速获取、删除、更新对应的“值对象”。

列表中我们通过“下标数字”找到对应的对象，字典中通过“键对象”找到对应的“值对象”。

“键”：是任意的不可变数据，比如：整数、浮点数、字符串、元组。但是：列表、字典、集合这些可变对象，不能作为“键”。并且“键”不可重复。

“值”：可以是任意的数据，并且可以重复。

空字典表示方式：`{}`或`dict()`

## 创建字典

### 方式一： `{key:value}`

```python
# {key: value}

dict1 = {'one': 1, 'two': 2, 'three': 3}
print(dict1)
```

### 方式二： `dict()`

```python
# dict(zip(keys, values))
# 或 dict([(k, v), (k, v)])
# 或 dict(((k, v), (k, v)))

>>> k = ['one', 'two', 'three']
>>> v = [1, 2, 3]
>>> dict2 = dict(zip(k, v))
>>> print(dict2)
{'one': 1, 'two': 2, 'three': 3}

>>> dict3 = dict([('one', 1), ('two', 2), ('three', 3)])
>>> print(dict3)
{'one': 1, 'two': 2, 'three': 3}
>>> dict3 = dict((('one', 1), ('two', 2), ('three', 3)))
>>> print(dict3)
{'one': 1, 'two': 2, 'three': 3}
```

### 方式三： `dict(key=value)`

```python
>>> dict4 = dict(one=1, two=2, three=3)
>>> print(dict4)
{'one': 1, 'two': 2, 'three': 3}
```

### 方式四： 字典推导式

```python
>>> lst1 = ['one', 'two', 'three']
>>> lst2 = [1, 2, 3]
>>> dict5 = {lst1[i]: lst2[i] for i in range(len(lst1))}
>>> print(dict5)
{'one': 1, 'two': 2, 'three': 3}
```

### 方式五： `fromkeys()`

```python
# 没有指定 value， 默认 None
dict6 = dict.fromkeys(['k1', 'k2', 'k3'])
print(dict6)  # {'k1': None, 'k2': None, 'k3': None}
# 指定 value
dict7 = dict.fromkeys(['k1', 'k2', 'k3'], 'value')
print(dict7)  # {'k1': 'value', 'k2': 'value', 'k3': 'value'}
```

## 访问字典元素

```python
# 定义一个字典
a = {'name': 'Lucy', 'age': 18, 'job': 'programmer'}
```

1. 通过[键]获得“值”。若键不存在，则抛出异常

	```python
	>>> a = {'name': 'Lucy', 'age': 18, 'job': 'programmer'}
	>>> print(a['name'])
	Lucy
	>>> print(a['sex'])
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	KeyError: 'sex'
	```

2. 通过 `get()`方法获得“值”。优点是: 指定键不存在，返回 None；也可以设定指定键不存在时默认返回的对象。推荐使用`get()`获取“值对象”。

	```python
	>>> a = {'name': 'Lucy', 'age': 18, 'job': 'programmer'}
	>>> print(a.get('sex', '不存在此键'))
	不存在此键
	```

3. 列出所有的键值对

	```python
	>>> for k, v in a.items():
	...     print(k, v)
	...
	name Lucy
	age 18
	job programmer
	```

4. 列出所有的键，列出所有的值

	```python
	>>> for k in a.keys():
	...     print(k)
	...
	name
	age
	job
	```

5. 检测一个“键”是否在字典中

	```python
	>>> for v in a.values():
	...     print(v)
	...
	Lucy
	18
	programmer
	```

## 字典元素添加

给字典新增“键值对”，如果“键”已经存在，则覆盖旧的键值对；如果“键”不存在，则新增”键值对“

```python
>>> a['addr'] = '上海市'
>>> print(a)
{'name': 'Lucy', 'age': 18, 'job': 'programmer', 'addr': '上海市'}
```

### `update()`

```python
# 更新，有则覆盖，无则添加
# 1. 增加键值对
# 方式一：
>>> dict9 = {'name': 'lucy', 'age': 18}
>>> dict9.update(hobby="运动", hight=178)
>>> print(dict9)
{'name': 'lucy', 'age': 18, 'hobby': '运动', 'hight': 178}

# 方式二：
>>> dict10 = {'name': 'lucy', 'age': 18}
>>> dict10.update([('hobby', '运动'), ('hight', 178)])
>>> print(dict10)
{'name': 'lucy', 'age': 18, 'hobby': '运动', 'hight': 178}

>>> dic10 = {'name': 'lucy', 'age': 18}
>>> dic10.update((('hobby', '运动'), ('hight', 178)))
>>> print(dict10)
{'name': 'lucy', 'age': 18, 'hobby': '运动', 'hight': 178}

# 方式三：
>>> dic11 = {'name': 'lucy', 'age': 18}
>>> dic12 = {'name': 'tom', 'hight': 178}
>>> dic11.update(dic12)
>>> print(dic11)
{'name': 'tom', 'age': 18, 'hight': 178}

# 2. 修改键所对应的值
>>> dict13 = {'name': 'lucy', 'age': 18}
>>> dict13.update(name='tom')
>>> print(dict13)
{'name': 'tom', 'age': 18}
```

### `setdefault(key, default)`

```python
# setdefault(key, default)
# 如果 default 省略，向字典中添加了 key: None
# 如果 default 未省略，则向字典中添加 key: default
>>> dict1 = {"name": "张三", "age": 18, "score": 100, "hobby": "篮球"}
>>> print(dict1)
{'name': '张三', 'age': 18, 'score': 100, 'hobby': '篮球'}
>>> dict1.setdefault("111")
>>> print(dict1)
{'name': '张三', 'age': 18, 'score': 100, 'hobby': '篮球', '111': None}
>>> dict1.setdefault("222", 222)
222
>>> print(dict1)
{'name': '张三', 'age': 18, 'score': 100, 'hobby': '篮球', '111': None, '222': 2
22}
```

## 字典元素删除

### `pop()`

删除指定键值对, 并返回对应的“值对象”.

```python
>>> a = {'name': 'Lucy', 'age': 18, 'job': 'programmer'}
>>> b = a.pop('age')
>>> print(b)
18
>>> print(a)
{'name': 'Lucy', 'job': 'programmer'}
```

### `popitem()`

随机删除一个键值对,并返回. 

```python
>>> a = {'name': 'Lucy', 'age': 18, 'job': 'programmer'}
>>> b = a.popitem()
>>> print(b)
('job', 'programmer')
```

==若想一个接一个地移除并处理项, 这个方法就非常有效.==

```python
>>> a = {'name': 'Lucy', 'age': 18, 'job': 'programmer'}
>>> for i in range(len(a)):
...     a.popitem()
...
('job', 'programmer')
('age', 18)
('name', 'Lucy')
>>> print(a)
{}
```

### `clear()`

删除所有键值对

```python
>>> a = {'name': 'Lucy', 'age': 18, 'job': 'programmer'}
>>> a.clear()
>>> print(a)
{}
```

### `del`

```python
>>> a = {'name': 'Lucy', 'age': 18, 'job': 'programmer'}
>>> del a['name']
>>> print(a)
{'age': 18, 'job': 'programmer'}
```

## 字典的其他方法

### `copy()`

```python
>>> import copy
>>> dict4 = {"name": "张三", "age": 18, "score": 100, "hobby": "篮球"}
>>> print(dict4)
{'name': '张三', 'age': 18, 'score': 100, 'hobby': '篮球'}
>>> dict5 = dict4.copy()
>>> dict4['name'] = 'jack'
>>> print(dict4)
{'name': 'jack', 'age': 18, 'score': 100, 'hobby': '篮球'}
>>> print(dict5)
{'name': '张三', 'age': 18, 'score': 100, 'hobby': '篮球'}
>>> print(dict5 is dict4)
False
```

思考问题：列表和字典的拷贝

```python
>>> list1 = [1, 2, 3, {"name": "张三", "age": 18}]
>>> list2 = list1.copy()
>>> list1[-1]['age'] = 20
>>> print(list2)
[1, 2, 3, {'name': '张三', 'age': 20}]	# 浅拷贝只


>>> list1 = [1, 2, 3, {"name": "张三", "age": 18}]
>>> list2 = copy.deepcopy(list1)
>>> list1[-1]['age'] = 20
>>> print(list2)
[1, 2, 3, {'name': '张三', 'age': 18}]


>>> dict4 = {"hobby": ["篮球"]}
>>> print(dict4)
{'hobby': ['篮球']}
>>> dict5 = dict4.copy()
>>> dict4['hobby'].append('足球')
>>> print(dict5)
{'hobby': ['篮球', '足球']}
```



## 序列解包（拆包）

序列解包可以用于元组、列表、字典，可以让我们方便的对多个变量赋值

```python
>>> x, y, z = (10, 20, 30)		# 换成列表也可
>>> x
10
>>> y
20
>>> z
30
```

序列解包用于字典时，默认是对“键”进行操作；如果需要对键值对操作，则需要使用`items()`; 如果需要对“值”进行操作，则需要使用`values()`

```python
di = {'name': 'Lucy', 'age': 18, 'job': 'programmer'}
a, b, c = di
print(a, b, c)		# name age job

a, b, c = di.items()
print(a)		# ('name', 'Lucy')

a, b, c = di.values()
print(a)		# Lucy
```













