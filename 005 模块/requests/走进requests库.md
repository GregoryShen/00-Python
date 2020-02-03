# 走进Requests库

## 第1章 走进Requests库

### 1-1 课程路线图

### 1-2 认识Requests库

### 1-3 学好Requests库的意义

### 1-4 环境准备

## 第2章 了解HTTP 协议

### 2-1 了解HTTP 协议原理

##### 什么是HTTP 协议

* HyperText
* dddd

秦朝统一度量衡的例子。建立一套协议，资源与资源之间的交流。互联网的基石就是通过HTTP协议，

### 2-2 简单的小程序-urllib

### 2-3 简单的小程序-requests

我们已经写了urllib_demo.py

打开这样url, 此时引入requests, 我们需要一点点修改一下,

第一个方法,u



如果要get一个对象,

response = requests.get(URL_IP)

访问对象非常简单,能map到外部

如果要是,编码解码方法,只需要调用它的方法,

这个时候,我们就是使用简单的requests, 运行,

python 

效果一模一样

此时我看到Content

接下来修改带参数的请求, 首先需要构建请求参数,

这时候没有构建参数这一步, 直接赋给一个叫params的变量

发送请求的时候也比较方便,后面的参数可以用,

接下来处理相应,

如果到打印status code, 

如果是个`json`对象的话, 可以编译一个`json`对象

然后运行一下这个文件,

不是json的话,就直接透明化了,因此,除了处理响应,

这就是requests的

发送请求就写什么样的方法,处理请求的时候,这种含义就很清晰,要稍微清晰一些,

带参数的请求更加方便, 如果后面, 这就是一个简单小程序

socket 比如获取了内容长度,这时候就把

因为有urllib3的支持,多次,这时候可以消耗更少的资源,比如访问github,如果大家RFC7230-

第二章小结

2.1 了解HTTP协议

2.2 简单的urllib小程序

2.3 简单的rquests

Readability counts

一目了然的

## 第3章 发送请求

### 3-1 请求方法

3.0 GitHub API

为了帮助我们去理解怎么去发送一个requests,

URL:https://developer.github.com/

这些本身是没有用户体系的,OAuth, API都在相关的

怎么操作这些资源,这些资源,怎么跟他去做一些互动

这就是第三章我们将会互动的

GET: 查看资源

POST: 增加资源

PUT: 修改资源

DELETE: 删除资源

HEAD: 查看相应头

​		  相当于get,首先它的响应速度

OPTIONS: 查看可用请求方法

使用requests库的方法也特别直接

第一个 除了endpoint, 能够让我们看到

### 3-2 带参数的请求

### 3-3 请求异常处理

### 3-4 自定义Request

## 第4章 处理相应

### 4-1 响应基本api

### 4-2 下载图片

我们利用response的基本API,我们做一些实战性的小任务.

* 利用爬虫自动下载图片

比如说一个很简单的任务,可能你会做一个爬虫,这时候拿个爬虫之后你需要去自动下载一个图片,那么你怎么去自动下载这个图片呢?我们都知道手动下载图片很简单,搜完之后另存为这样下载图片,这样下载图片速度太慢了,我们希望利用Requests这个库帮我们简化工作

* 远程下载服务器上的文本文件

如果你在一个服务器上放了一个很大的csv文件,你需要远程把它拖下来,那这个文件也是可以通过http传输的方式进行相应的传输

我们接下来用一个很简单的小例子告诉大家怎么去下载这样的文件

百度随便搜一个图片跟GitHub相关的图片,然后右键在新标签页打开,得到一个`.jpg`结尾的图片地址.

新起一个文件,文件的名字叫做`img_response.py`.

新建一个方法叫做`download_image`,这个方法的主要功能也是帮我们下载图片的.

第一个我们肯定要知道它的`url`,在刚才的网页中已经看到了,我们把它直接拿过来,然后看看response(刚才是通过浏览器发出的`get`请求),就是用`requests`库,先把`requests`库引入进来,通过`requests`库`get`一下`url`这个地址;之后打印一下`response`的`content`信息,看看`content`信息到底是什么

```python
import requests

def download_image():
    """demo:下载图片
    """
    url = '刚才的那个地址'
    response = requests.get(url)
    print(response.content)
    
download_image()
```

返回一个`403 - Forbidden`,即没有权限去访问.对比浏览器,直接打开就可以获得图片,此时需要关注一下这个`response`的状态码,原因是什么,然后再看下`response`的`headers`是什么,这个时候我们已经知道`content`已经不是我们想要的内容了

```python
import requests

def download_image():
    """demo:下载图片
    """
    url = "刚才的url"
    response = requests.get(url)
    print(response.status_code, response.reason)
    print(response.headers)
    # print(response.content)
    
download_image()
```

再运行下程序,得到结果:

```shell
403 Forbidden
{'Date': 'Mon, 18 Jul 2016 14:26:56 GMT', 'Content-Length': '345', 'Content-Type': 'text/html', 'Server': 'lighttpd'}
```

我们看下浏览器的F12,我们发现我们的`User-Agent`是`requests`,它拒绝了这样的`User-Agent`,如果我们把浏览器的`User-Agent`盗用过来,是否能把图片下载下来呢?实践一下:

我们加一个`headers`的信息,刚才我们没加的时候`User-Agent`其实是`Python-requests`,这时候我们伪造一个类似于浏览器的`User-Agent`.

这时候在请求后面缀上`headers=headers`,就是让它相信我们这是一个从浏览器发出的请求:

```python
import requests

def download_image():
    """demo:下载图片
    """
    headers = {刚才复制的浏览器里的'User-Agent'}
    url = "刚才的那个网址"
    response = requests.get(url, headers=headers)
    print(response.status_code, response.reason)
    print(response.headers)

download_image()
```

这个时候`status_code`和`reason`马上变了,变成了`200 OK`

这时候`'Content-Type'`也变了,变成了`'image/jpeg'`,它是一个图片的格式.

这时候试试我们能不能把图片直接打印出来

```python
import requests

def download_image():
    """demo:下载图片
    """
    headers = {刚才复制的浏览器里的'User-Agent'}
    url = "刚才的网址"
    response = requests.get(url, headers=headers)
    print(response.content)
```

结果是一片乱码,说明这个东西不能被`content`直接来解析,乱码就像是一个流一样,我们就要换成`raw`的方式来解析,`raw`的方式就是在`requests`里要支持流传输,流传输就相当于打开这样一个链接,相当于它是跟流一样让文件以比特流一个个流过来,然后把这个流再去像读文件一样转存到本地的文件.

这时候可以在本地打开一个叫`demo.jpg`的文件,用写入的方式(`wb`), 这是一个file,根据`response`(`response`里面其实还有一个API叫做`iter_content`,可以去遍历它所有的内容,可以给它一个遍历的大小,比如128个遍历一次),然后把它写入文件地址(一个小的`chunk`),也就是一块一块地把它写到`demo.jpg`里面.

```python
import requests

def download_image():
    """demo:下载图片
    """
    headers = {刚才复制浏览器里的'User-Agent'}
    url = "刚才的网址"
    response = requests.get(url, headers=headers, stream=True)
    with open('demo.jpg', 'wb') as fd:
        for chunk in fd.iter_content(128):
            fd.write(chunk)
            
download_image()
```

再次运行这个文件,此时看看会不会这里面出现一个`demo.jpg`.

稍作等待以后果然出现了`demo.jpg`.用`open demo.jpg`的方式打开查看图片是否为期待的图片.我们用这种方式就把它下载下来了.

如果要用`requests`库下载图片或下载其他的文件,千万不要就直接想当然的用`content`,我们说文本用`content`,用`json`文本都可以看,但是有些`Content-Type`它不一样,所以这种`Content-Type`最好用上面的方式去做.

再推荐一种方式,因为建立这个流,这个流其实在`requests`里是打开的,没有把这个流关掉.

1. 伪造headers 信息
2. 限定URL,这时候就生成了一个response

这时候通过引入另一个东西,在Python里面其实有很多的很小的语法糖,比如说`contextlib`,它就是专门来管上下文信息的,可以让它自动close掉请求和相应.把`response`的内容挪近close里作为参数,这时候对于我来说这是一个流,这个流已经读完之后,应该把它关掉;上一个方法没那么做,还是保持了这个链接,这时候会消耗一些资源,我们用这样一个管理上下文的方式就合理地避免了这一点.

3. 打开文件

接下来还是跟前面一样,依然可以通过读取这个response来做后面的操作,

4.每128就写入一次

生成文件之后,来一个个去写入

这个和上面的区别就是增加了一个上下文的语境,因为这种方式是流传递,所以需要把这个流关掉.

运行和验证方法与前述方法相同.

简单回顾一下,刚才我们做的一个小小的改动,也就是在打开文件之前,,我们把response(因为它是经过`stream`来传输的)做了一个上下文,在它打开这样一个传输流之后,记得最后把它关上.

用一个流程图简单梳理一下:

**浏览器模拟**

​	  你可以通过浏览器自带的开发者工具了解一下请求是怎么发出来的

**构建request**

​	  自己想办法把它构建成一个requests对象,这个过程中发出去经过简单的探索发现不行,只有不断去调试直到requests对象是我们想要的对象,比如刚才就是伪造了一下它的`headers`

**读取流data**

​	  接下来就是读取流的这样一个数据,因为文件都是流的

**存入数据**

​	  之后开启一个文件并且把它存入数据,存成一个文件模式.

这就是如何利用reqeusts把它的response对象存成图片或者文件

### 4-3 事件钩子

 比如用github或gitlab,比如去push,可以稍微改变一下

开发模式是基于回调的

线性处理

就像“非线性叙事”一样

我要怎么样才能触及到服务器,等这样的一个IO,整个模型就特别简单了,

```python
import requests


def main()
```

在我们主程序中,访问一下百度, 挂在钩子上, 可以注册一个字典, 我要注册一个响应的函数进去, 我想 这就不是线性的,

这时候我又在前面添加一个回调函数,首先回调函数, 我们主要是拿response对象说事, 我想知道他headers里面的content-type是什么, 这个跟我

让我们更好的管理, 这样一些函数, 如果直接执行,

我们知道百度这个首页, 我们也可以换一个, http://api.github.com

再次运行这个小程序, 就是`application/json`

整个程序更有好处

等到,打开了一个新的视角, 

Complexis better than complicated.

Complex 可能是问题本身的复杂度,

## 第5章 进阶话题

### 5-1 HTTP 认证

http所有的东西都可以看见, 有些情况下,除了花的主人,因为里面会存在很多安全性的问题,就像这些, 学习http之后,我们怎样完成这个http认证

server怎么知道

接下来 server端 请你提供账号和密码送给你

服务器端验证或内存里,接下来就返回它要的资源,

在requests库里面auth关键字

```python
import requests

def construct_url(end_pint)

def basic_auth():
    """
    基本认证
    """
    response = requests.get()
    print(response.text)
    print(response.request.headers)
    
basic_auth()
```

运行一下这个小程序, 因为这个是唯一属于我,不属于

进入一个交互显示器,

进行一个b64的decode,

```python
>>> import base64
>>>
```

基本认证有好处,

OAUTH认证

以GitHub为例, 相当于对GitHub来说是个应用,

它需要去获取哪些账号信息, Public data only, 

经过这么一步,你会发现,它做了一个oauth认证,

首先第一步, 注册一个app编号, 以及app想要获取的scope信息,相当于

app拿到这个access_token, 这个时候codewars对他来说是透明的, 和自己

最底层方式,有一个personal access token, 还可以限定获取哪些资源,这个时候就描述清楚这个, 

```python
def basic_oauth():
    headers = {'Authorization': 'token '}
    
```

首先给他一个response, headers就把自己带上, 获取认证的过程

首先要和GitHub

打印一下request的headers是什么

简单运行一下这个文件, 

我们其实有更好的方法,

```python
from requests.auth import AuthBase

class GithubAuth(AuthBase):
  
    def 
```

### 5-2 Proxy代理



### 5-3 Session和Cookie

HTTP是一种无状态的响应,就是一个请求过去,和下一个请求没有任何关系.但是经常有很多应用需要让两个有关系,比如你已经是个登录用户了,你现在已经把一些东西加入到购物车,那不能说跳转个页面购物车东西没了,因为你是没有状态的,所以这时候需要两种机制来解决:一个是session一个是cookie

session位于服务器端来存储一些用户信息,去保留这种状态;cookie是浏览器端来存储

首先来看看cookie的存储原理:

1. 浏览器首先发送一个HTTP请求(无cookie),它是第一个请求所以没有任何cookie,











