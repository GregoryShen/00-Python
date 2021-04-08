# [超详细Python字符串用法大全](https://mp.weixin.qq.com/s/tKLRfVojpSDtszW5SmF3SQ)

## 字符串拼接

实际场景: 把列表中的数据拼接成一个字符串

解决方案: 使用 `str.join()` 方法

```python
>>> li = ['cxk', 'cxk', 'kk', 'caibi']
>>> ''.join([str(i) for i in li])
'cxkcxkkkcaibi'
```

推荐使用生成器表达式, 如果列表很大, 可以节省很多内存空间

```python
>>> ''.join(str(i) for i in li)
'cxkcxkkkcaibi'
```

## 拆分含有多种分隔符的字符串

实际场景: 把某个字符串一句分割符号拆分不同的字段, 该字符串包含多种不同的分隔符

```python
s = "ab;fd/ft|fs,f\tdf.fss*dfd;fs:uu}fsd"
```

1. 使用 python 中的 split() 方法, 由于 split 一次处理一个分隔符, 例如:

```python
>>> res = s.split(';')
>>> res
['ab', 'fd/ft|fs,f\tdf.fss*dfd', 'fs:uu}fsd']
```



# [你真的知道Python的字符串怎么用吗？](https://mp.weixin.qq.com/s/M4_38VHlQwp-CDRczh2NIA)

 Python 中字符串是由 Unicode 编码的字符组成的不可变序列, 它具备与其他序列共有的一些操作, 例如判断元素是否存在、拼接序列、切片操作、求长度、求最值、求元素的索引位置及出现次数等等.

本文主要介绍 Python 字符串特有的操作方法, 比如它的拼接、拆分、替换、查找及字符判断等使用方法, 辨析了一些可能的误区. 最后, 还做了两个扩展思考: 为什么它不具备 Java 字符串的一些操作呢? 

## 拼接字符串

七种拼接方式从实现原理上划分为三类, 即格式化类(%占位符、format()、template)、拼接类(+操作符、类元组方式、join()) 与插值类(f-string), 在使用上, 有如下建议:

当要处理字符串列表等序列结构时, 采用 join() 方式; 拼接长度不超过20时, 选用+号操作符方式; 长度超过20的情况, 高版本选用 f-string, 低版本时看情况选用 format() 或 join() 方式.

还有一种字符串乘法, 可以重复拼接自身.

在复杂场景下, 尽量避免使用以上几类原生方法, 而应该使用外置的强大的处理库. 比如在拼接 SQL 语句的时候,经常要根据不同的条件分支, 来组装不同的查询语句, 而且还得插入不同的变量值, 所以当面临这种复杂的场景时, 传统拼接方式只会加剧代码的复杂度、降低可读性和维护性. 使用 SQLAlchemy 模块, 将有效的解决这个问题.

## 拆分字符串

在字符串的几种拼接方法中, `join()` 方法可以将列表中的字符串元素拼接成一个长的字符串, 与此相反, `split()` 方法可以将长字符串拆分成一个列表. 前面已经说过, 字符串是不可变序列, 所以字符串拆分过程是在拷贝的字符串上进行, 并不会改变原有字符串.

`split()` 方法可以接收两个参数, 第一个参数是分隔符, 即用来分隔字符串的字符, 默认是所有的空字符, 包括空格、换行(\n)、制表符(\t)等. 拆分过程会消耗分隔符, 所以拆分结果中不包含分隔符.

```python
s = 'Hello world'
l = '''Hi there , my name is     Python猫
Do you like me ?
'''

# 不传参数时, 默认分隔符为所有空字符
>>> s.split()
['Hello', 'world']
>>> s.split(' ')		# 以一个空格为分隔符
['Hello', 'world']
>>> s.split('  ')		# 以两个空格为分隔符
['Hello world']
>>> s.split('world')
['Hello ', '']
>>> l.split()			# 空字符包括空格、多个空格、换行符等
['Hi', 'there', ',', 'my', 'name', 'is', 'Python猫', 'Do', 'you', 'like', 'me', '?']
```

`split()` 方法等第二个参数是一个数字, 默认是缺省, 缺省时全分隔, 也可以用 `maxsplit` 来指定拆分次数

```python
# 按位置传参
>>> l.split(' ', 3)
['Hi', 'there', ',', 'my name is     Python猫\nDo you like me ?\n']

# 指定传参
>>> l.split(maxsplit=3)
['Hi', 'there', ',', 'my name is     Python猫\nDo you like me ?\n']

# 错误用法
>>> l.split(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must be str or None, not int
```

`split()` 方法是从左往右遍历, 与之相对, `rsplit()` 方法是从右往左遍历, 比较少用, 但是会有奇效

拆分字符串还有一种方法, 即 `splitlines()`, 这个方法会按行拆分字符串, 它接收一个参数 True 或 False, 分别决定换行符是否会被保留, 默认值 False, 即不保留换行符.

```python
>>> 'ab c\n\nde fg\rkl\r\n'.splitlines()
['ab c', '', 'de fg', 'kl']
>>> 'ab c\n\nde fg\rkl\r\n'.splitlines(True)
['ab c\n', '\n', 'de fg\r', 'kl\r\n']
>>>
```



# 数据类型和编码相关问题

## [java基础类型中的java基础类型中的char和byte的辨析及Unicode编码和UTF-8的区别](https://www.cnblogs.com/lingyejun/p/9743788.html)

### `char`和`byte`的对比

> byte

byte字节,数据存储容量1byte, byte 作为基本数据类型表示的也是一个存储范围上的概念, 有别于int/long 等专门存数字的类型, 这种类型的大小就是1 byte,而int 是4byte.

存数字的话就是1byte=8位, 2^8=256即-128~127.字符的话包括字母和汉字, 一个字母是1byte, 一个汉字是2byte.也就是可以用byte变量去存储一个英文字符,但是却存不下一个中文汉字,因为一个汉字占2byte.

总结,byte 是Java 中的一个基本数据类型,这个数据类型的长度是1byte,此byte就是彼byte,既是基本数据类型也是存储空间的基本计量单位,

> char

`char`是Java中的保留字,与别的语言不同的是,char 在Java 中是16位的,因为Java 用的是Unicode. 不过8位的ascii码包含在Unicode 中, 是从0~127的.

Java 中使用Unicode的原因是,Java的applet允许全世界范围内运行,那就需要一种可以表述人类所有语言的字符编码, Unicode.

`char`本质上是一个固定占用两个字节的无符号正整数,这个正整数对应于Unicode编号,用于表示那个Unicode 编号对应的字符.

由于固定占用两个字节,char 只能表示Unicode 编号在65536以内的字符,而不能表示超出范围的字符.

### Unicode 和 UTF-8 的对比

> Unicode

需要注意的是, Unicode 只是一个符号集, 它只规定了符号的二进制代码,却没有规定这个二进制代码该如何存储.

比如,汉字“严”的Unicode 是十六进制数4E25, 转换成二进制数足足有15位, 也就是说这个符号的表示至少需要2个字节.表示其他更大的符号,可能需要3个字节或者4个字节,甚至更多.

这里就有两个严重的问题,第一个问题是,如何才能区别Unicode 和ASCII? 计算机怎么知道三个字节表示一个符号,而不是分别表示3个符号呢? 第二个问题是,我们已经知道,英文字母只用一个字节表示就够了,如果Unicode 统一规定,每个符号用3个或4个字节表示, 那么每个英文字母前都必然有2到3个字节都是0,这对于存储来说是极大的浪费,文本文件的大小会因此大出两三倍,这是无法接受的,他们造成的结果是:

1) 出现了Unicode 的多种存储方式,也就是说有许多种不同的二进制格式可以用来表示Unicode

2) Unicode 在很长一段时间内无法推广, 直到互联网的出现

> UTF-8

互联网的普及,强烈要求出现一种统一的编码方式, UTF-8就是互联网上使用最广的一种Unicode 实现方式. 其他实现方式还包括UTF-16(字符用两个字节或四个字节表示)和UTF-32(字符用4个字节表示). UTF-8是Unicode 的实现方式之一

utf-8是一个变长编码标准,可以用1~4个字节表示一个字符, 而中文占3个字节,ascii 字符占1个字节

> 为什么我们在Java里面可以用一个char 来表示一个中文呢?

因为Java 是以Unicode 作为编码方式的. Unicode 是一个定长的编码标准, 每个字符都是2个字节,也就是1个 char类型的空间. 在编译的时候会把utf-8的中文字符转换成对应的Unicode 来进行传输运算

```java
import java.io.UnsupportedEncodingException;

public class ChineseCharCode {
  
    public static void main(String[] args) {
        String str = '中';
        char c = '中';
        // Java 使用Unicode编码,一个字符占两个字节
        System.out.println("char字符 中 二进制"+Integer.toBinaryString(c));
        try {
            // utf-8是Unicode 的实现方式之一
            System.out.println(str.getBytes('UTF-8').length);
            // utf-16也是Unicode 的实现方式之一, 但使用较少
            System.out.println(str.getBytes("UTF-16").length);
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        }
    }
}
```

























