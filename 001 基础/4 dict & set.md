[廖雪峰：使用dict和set](https://www.liaoxuefeng.com/wiki/1016959663602400/1017104324028448)

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

#### set

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

[Python3 字典](https://www.runoob.com/python3/python3-dictionary.html)

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



你知道和不知道的Python字典都在这里！！

https://mp.weixin.qq.com/s/36_gHzFKpQ9rIscFOfUboQ





















