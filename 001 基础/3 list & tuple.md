# 廖雪峰

## 使用list和tuple

### list

Python内置的一种数据类型是列表：list。list是一种==有序==的==集合==，可以随时添加和删除其中的元素

比如，列出班里所有同学的名字，就可以用一个list表示：

```python
>>> classmates = ['Michael', 'Bob', 'Tracy']
>>> classmates
['Michael', 'Bob', 'Tracy']
```

变量classmates就是一个list。<u>**用`len()`函数可以获得list元素的个数**</u>

```python
>>> len(classmates)
3
```

用索引来访问list中每一个位置的元素，记得索引是从0开始的

当索引超出了范围时，Python会报一个`IndexError`错误，所以，要确保索引不要越界，最后一个元素的索引是`len(classmates) - 1`

如果要取最后一个元素，除了计算索引位置之外，还可以用-1做索引，直接获取最后一个元素。一次类推，可以获取倒数第2个、倒数第3个

倒数第4个就越界了

list是一个可变的有序表，所以，可以往list中追加元素到末尾：

```python
>>> classmates.append('Adam')
```

也可以把元素插入到指定位置，比如索引为1的位置：

```python
>>> classmates.insert(1, 'Jack')
```

要删除list末尾的元素，用`pop()`方法

要删除指定位置的元素，用`pop(i)`方法，其中i是索引位置

要把某个元素替换成别的元素，可以直接赋值给对应的索引位置

list里面的元素的数据类型也可以不同

list元素也可以是另一个list

如果一个list中一个元素也没有，就是一个空的list，它的长度为0

```python
>>> L = []
>>> len(L)
0
```



[Python 列表(List)](https://www.runoob.com/python/python-lists.html)

[Python list 操作](https://www.cnblogs.com/zhengyuxin/articles/1938300.html)

[Python 列表(Lists)](https://www.w3cschool.cn/python/python-lists.html)

[Python List list()方法](https://www.runoob.com/python/att-list-list.html)

[Python列表（list）的基本用法](https://blog.csdn.net/laobai1015/article/details/85126659)

[python中对list去重的多种方法](https://www.cnblogs.com/nyist-xsk/p/7473236.html)

[Python list列表删除元素（4种方法）](http://c.biancheng.net/view/2209.html)

[python中list的五种查找方法](https://blog.csdn.net/qq_31747765/article/details/80944227)



[Python3 元组](https://www.runoob.com/python3/python3-tuple.html)

[Python 元组(Tuple)操作详解](https://www.jb51.net/article/47986.htm)



