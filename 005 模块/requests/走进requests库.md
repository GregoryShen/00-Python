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

比如说一个很简单的任务,可能你会做一个爬虫,这时候拿个爬虫之后你需要去自动下载一个图片,那么你怎么去自动下载这个图片呢?我们都知道手动下载图片很简单,比如上百度随便搜一个图片,搜完之后右键另存为把它整理在我的文件夹里,这样下载图片速度太慢了,我们希望利用`requests`这个库帮我们简化工作

* 远程下载服务器上的文本文件

如果你在一个服务器上放了一个很大的`csv`文件,你需要远程把它拖下来,那这个文件也是可以通过`HTTP`传输的方式进行相应的传输

我们接下来用一个很简单的小例子告诉大家怎么去下载这样的文件

百度随便搜一个图片跟`GitHub`相关的图片,然后右键在新标签页打开,得到一个`.jpg`结尾的图片地址.

新起一个文件,文件的名字叫做`img_response.py`.

新建一个方法叫做`download_image`,这个方法的主要功能是帮我们下载图片的.

第一个我们肯定要知道它的`url`(在刚才的网页中已经看到了,我们把它直接拿过来),我们这时候想去看看它的`response`(刚才我们通过浏览器,浏览器其实也就是发了出`get`请求),我们就是用`requests`这个库,先把`requests`库引入进来,通过`requests`库去`get`一下这个`url`地址;之后打印一下`response`的`content`信息,看看`content`信息到底是什么

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

返回一个`403 - Forbidden`,即没有权限去访问.对比浏览器,直接打开就可以获得图片,此时需要关注一下这个`response`的`status_code`是什么,这相当于是一种探索,它的`reason`是什么,然后再看下`response`的`headers`是什么,这个时候我们已经知道`content`已经不是我们想要的内容了

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

我们看下浏览器,思考一下浏览器是怎么做的,调出浏览器的开发者模式,我们发现有一个地方和我们的程序很不一样,我们的`User-Agent`是`requests`,它拒绝了这样的`User-Agent`,如果我们把浏览器的`User-Agent`盗用过来,是否能把图片下载下来呢?实践一下:

打开脚本,我们加一个`headers`的信息,刚才我们没加的时候`User-Agent`其实是`Python-requests`,这时候我们伪造一个类似于浏览器的`User-Agent`.

这时候在请求后面缀上`headers=headers`,就是让它相信我们这是一个从浏览器发出的请求:

```python
import requests

def download_image():
    """demo:下载图片
    """
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'}
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
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'}
    url = "刚才的网址"
    response = requests.get(url, headers=headers)
    print(response.content)
```

结果是一片乱码,说明这个东西不能被`content`直接来解析,乱码就像是一个流一样,我们就要换成raw的方式来解析,raw的方式就是在`requests`里让它去支持流传输,流传输就相当于打开这样一个链接,相当于它是跟流一样让文件以比特流一个一个流过来,然后把这个流再去像读文件一样转存到本地的文件.

这时候可以在本地打开一个叫`demo.jpg`的文件,用写入的方式(`wb`), 这是一个file,根据`response`(`response`里面其实还有一个API叫做`iter_content`,可以去遍历它所有的内容,可以给它一个遍历的大小,比如是128个遍历一次),然后把它写入文件地址(一个小的`chunk`),也就是一块一块地把它写到`demo.jpg`里面.

```python
import requests

def download_image():
    """demo:下载图片
    """
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'}
    url = "刚才的网址"
    response = requests.get(url, headers=headers, stream=True)
    with open('demo.jpg', 'wb') as fd:
        for chunk in response.iter_content(128):
            fd.write(chunk)
            
download_image()
```

再次运行这个文件,此时看看会不会这里面出现一个`demo.jpg`.

稍作等待以后果然出现了`demo.jpg`.用`open demo.jpg`的方式打开查看图片是否为期待的图片.我们用这种方式就把它下载下来了.

如果要用`requests`库下载图片或下载其他的文件,千万不要就直接想当然地用`content`,我们说文本用`content`,用`json`文本都可以看,但是有些`Content-Type`它不一样,所以这种`Content-Type`最好用上面的方式去做.

再推荐一种方式,因为建立这个流,这个流其实在`requests`里是打开的,没有把这个流关掉.这是流传输的一种模式,再编写一种方法,叫做提升的一种方法,`download_image_improved`首先我也是利用它来下载图片,前面的都一样(`headers`,`url`,`response`),稍做一些注释,第一步就是伪造`headers`信息,第二步就是限定`URL`,这时候就生成了一个`response`

这时候通过引入另一个东西,在`Python`里面其实有很多很小的语法糖,比如说`contextlib`,它就是专门来去管上下文信息的,我可以让它自动去`close`掉请求和相应

把`response`的内容移过来作为`closing`的参数,这时候读完这个流就应该把它关掉,上一个方法其实没这么做,还是保持了这个链接,这时候会消耗一些资源,我们用这样一个管理上下文的方式就合理地避免了这一点.

接下来还是跟前面一样,依然可以通过读取这个`response`来做后面的操作,依然可以打开这样一个文件(添加注释:打开文件),生成文件之后一个一个写入(添加注释:每128写入一次),之后写入这样一个`chunk`就行了

```python
import requests

def download_image():
    '''demo:下载图片
    '''
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'}
    url = 'xxxx'
    response = requests.get(url, headers=headers, stream=True)
    with open('demo.jpeg', 'wb') as fd:
        for chunk in response.iter_content(128):
            fd.write(chunk)
            
            
def download_image_improved():
    '''demo: 下载图片
    '''
    # 伪造headers 信息
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'}
    # 限定url
    url = ''
    from contextlib import closing
    with closing(requests.get(url, headers=headers, stream=True)) as response:
        # 打开文件
        with open('demo1.jpeg', 'wb') as fd:
          # 每128写入一次
            for chunk in response.iter_content(128):
                fd.write(chunk)
```

这个和上面的区别就是增加了一个上下文的语境,因为这种方式是流传递,所以需要把这个流关掉.

这时候来调用一下这个方法`download_image_improved()`,按理说会在目录下出现一个`demo1.jpeg`

简单回顾一下,刚才我们做的一个小小的改动,也就是在打开文件之前做了一个上下文.我们把`response`(因为它是经过`stream`来传输的)做了一个上下文,在它打开这样一个传输流之后,记得最后把它关上.

用一个流程图简单梳理一下:

**浏览器模拟**

​	  你可以通过浏览器自带的开发者工具了解一下请求是怎么发出来的

**构建request**

​	  自己想办法把它构建成一个request对象,这个过程中发出去经过简单的探索发现不行,只有不断去调试直到request对象是我们想要的对象,比如刚才就是伪造了一下它的`headers`

**读取流data**

​	  接下来就是读取流的这样一个数据,因为文件都是流的

**存入数据**

​	  之后开启一个文件并且把它存入数据,存成一个文件模式.

这就是如何利用`reqeusts`把它的`response`对象存成图片或者文件

### 4-3 事件钩子

什么是钩子? 

​	  这种钩子在程序界特别流行,比如说用github或gitlab,有很多钩子函数,比如当你去`push`一个库的时候,它会自动去激发另一些东西.这种钩子都是事件驱动型开发,它可以稍微改变一下开发思路.最常见的就是JavaScript,它的很多开发模式都是基于回调的,这种回调就是事件完成之后它引起的一系列的动作.

事件钩子在`Requests`库里面也会有这种体现,一般处理`response`都是线性处理,比如说先发`request`,发完之后拿到响应,接下来再做其他的事情.就像一个编剧一样,他会把事件按照时间先后顺序一个一个垒起来.尝试把它全部打散,就像“非线性叙事法”一样,我们把它打散,放在不同的地方,就像事件钩子一样.

事件钩子整个过程是怎么样呢?

​	  首先,要在主程序中发起一个IO请求,比如像`requests`库,它就是发起了一个get或post或其他方式的IO请求,向互联网放出这样一个请求,我们要去等待,等待完之后,右边红色这一段就是我要怎样才能触及到服务器然后再回来.在主程序中我们会在发起请求的时候就注册一个这样的事件钩子,等这样一个IO请求结束之后它自动把`response`塞入到回调函数中,进行一个回调处理.

下面用一个很小的程序梳理一下

```python
import requests

def main():
    """主程序
    """
    requests.get('https://www.baidu.com', hooks=dict(response=get_key_info))
```

首先还是引入`requests`库.

接下来我们有一个主方法,这是我们的主程序.在主程序中,我们首先要做的就是`requests.get()`,比如我们就打印一下百度.等我们去发送一个`get`请求之后,我们想挂在它的钩子上,钩子在这个`requests`对象中我们就可以注册,它可以注册成一个字典函数,它的键就是`response`,当我接到这个`response`对象,我要注册一个相应的函数进去,那这个函数取个名字叫`get_key_info`,我想把它的一些关键性的信息能让我们很快地看到,这就不是线性的

```python
import requests

def get_key_info(response, *args, **kwargs):
    """回调函数
    """
    print(response.headers['Content-Type'])
    
def main():
    """主程序
    """
    requests.get('https://www.baidu.com', hooks=dict(response=get_key_info))
    
main()
```

这时候在前面再放一个函数,这个函数就是我们所谓的回调函数.拿到这个回调函数我们做了一件事情,首先回调函数会去接受几个参数,第一个参数就是`response`,其实还有其他相应的参数我们在这里不一一列出来,都把他们聚合在`*args`和`**kwargs`中间,我们主要是拿response对象说事.当这个钩子回来之后,我拿到这个`response`之后,我想知道它`headers`里面的`Content-Type`是什么,也就是它的这种内容的类型是什么,以便于我接下来做其他事情.

这时候用这种思路来去总结和组织的程序模式就和我们用线性的方式一气呵成地写下来的感觉是不一样的,因此这种方式提供了另一种可能性帮你更好的去管理.可能你在某些情况下会这样用,更好的去管理这样一些函数.

![截屏2020-02-0418.10.16](/Users/gregoryshen/Desktop/截屏2020-02-0418.10.16.png)

执行这个函数,就打印出来了,它是一个`text/html`.我们知道百度这个首页是这样一个内容类型.

除此之外我们也可以换一个 http://api.github.com,再次运行这个小程序, 按照预期就是`application/json`

![截屏2020-02-0418.13.29](/Users/gregoryshen/Desktop/截屏2020-02-0418.13.29.png)

这就是一个最简单的钩子函数的写法.它重新组织了怎么去解析`response`,我把`request`和`response`可以更加合理地放在不同函数之中进行管理.我们写一个小程序这倒无所谓,但是组织大型程序可能它会对你组织程序更加有好处.它帮我们打开了一个新的视角, 去做相应的处理.

Complex is better than complicated.

Complicated其实是很嘈杂的意思,在程序里面我们可以很嘈杂的写很多程序,就是写的很多乱七八糟的;Complex可能是问题本身的复杂度,问题本身的复杂度要比你把这个问题解释成很嘈杂要更好.

## 第5章 进阶话题

### 5-1 HTTP 认证

#### 为什么要进行HTTP认证?

我们之前所讲解的,发送一个请求,得到一个响应,其实有一个简单的假设,就是说通过HTTP通信我们看到的所有的资源对我们来说都是可见的,那么它就像一个没有围墙的花园一样,里面所有的东西都可以看见.但是有些特别情况下,我们需要给这些花园上加一把锁,这把锁是具有安全性的,比如说这个花园里种的某一束花我们不想让除了花的主人去操作去看它,因为里面会存在很多安全性的问题,所以我们需要认证出来这个拿着钥匙的人确实就是花园里面花的主人.

就像这幅图中的例子一样, 由于近几年网上会出现有一些网站的安全性不足导致用户个人的隐私信息被盗窃这样的事件.学习HTTP之后,我们也需要去思考一下,我们怎么样去完成这个HTTP认证.

#### HTTP基本认证

先说说最简单的,也就是在前4章提到过的,就是`client`和`server`之间怎么进行验证,`server`怎么知道`client`是一个合法的`client`:

```sequence
Client->Server:1.Requests a protected resource
Server->Client:2.Requests a username:password
Client->Server:3.Sends username:password
Server->Client:4.Returns requested resource
```

首先`Client`端发一个`requests`,一个被保护的资源,就像我们说花园里的一束花一样;那么接下来`Server`端说:你要去获得这个资源,那么请你提供你的账号和密码,这也是最基本的一种模式.那么客户端拿到这句话后说,我要把我账号密码送给你,然后就发送给`Server`端,服务器端说:应验证这个账号密码在`Server`端是否是匹配的,比如说`Server`端会去存在数据库里或存在任何内存里,然后发现这个账号密码是匹配的,那么接下来就返回它要求的资源,这就是最简单的一个HTTP基本认证.

对我们来说是在`requests`库里面有一个关键字`auth`,我们直接把`auth`加上就行了.我们具体看一个小例子:

这个小例子就是`authen.py`,提前的一些东西已经写好了,首先引入了`requests`库,我们依然使用GitHub这样一个API,然后来构建一个完整的URL:

```python
import requests

BASE_URL = 'https://api.github.com'

def construct_url(end_pint):
    return '/'.join([BASE_URL, end_point])
```

我们写一个很小的方法,叫做`basic_auth`,也就是基本认证,那肯定是要提供用户名和密码的,比如说`response`如果直接去往这个URL上,比如说去访问它的user资源,如果没有经过认证的话(就是向这样:`response = requests.get(construcl_url(‘user’))`)这边肯定会返回一个所谓的`401 未认证`的code,我们需要认证的话就在后面加一个`auth`信息,此时先打印一下最后的结果,也就是`response.text`,看下这个认证是怎么构建的,然后看一下`request`的`headers`信息, 然后在方法中直接使用`basic_auth`

```python
import requests

BASE_URL = 'https://api.github.com'

def construct_url(end_poinit):
    return '/'.join([BASE_URL, end_point])
  
def basic_auth():
  	'''基本认证
  	'''
    response = requests.get(construct_url('user'), auth=('imoocdemo', 'imoocdemo123'))
    print(response.text)
    print(response.request.headers)
    
basic_auth()
```

运行一下这个小程序, 这个程序是把用户名和密码输给了服务器,我想验证一下我就是我,看看能否识别出来,

![image-20200209195937354](/Users/gregoryshen/Library/Application Support/typora-user-images/image-20200209195937354.png)

首先我已经获取了我想要的资源,这可以说是被保护的资源,因为这是唯一属于这个账号的资源,如果不输入`auth`的话,出来的就是`401 未认证`.

`auth`主要做的工作就是在`request`的`headers`上加了:

![截屏2020-02-0920.03.20](/Users/gregoryshen/Desktop/截屏2020-02-0920.03.20.png)

是一个基本认证,后面一串码用一个很小的技巧就一目了然了,首先进入交互解释器,这个其实是一个base64的码,给它一个b64的`decode`,

```python
>>> import base64
>>> base64.b64decode('Z3JlZ29yeXNoZW50akBnbWFpbC5jb206c2hlbnhpbjIyMDE5ODkx')
```

![截屏2020-02-0920.15.33](/Users/gregoryshen/Desktop/截屏2020-02-0920.15.33.png)

这是`base64`的码,看上去好像是很有隐秘性,谁也看不懂,实际上用一般的程序,Python也好,Java也好都可以把它`decode`出来,解码出来它就是把`username`和`password`直接放在headers里面,那这样安不安全呢

#### OAUTH认证

基本认证有好处,它不会让HTTP请求变得那么不安全,但是它也不是很安全,接下来介绍一个更高级的,这个其实就是authorization的一个进阶模式`OAUTH`,`OAUTH`之后进阶到了`OAUTH2`.

以GitHub为例, 来解释一下`OAUTH`到底是什么,第三方网站相当于对GitHub来说是个应用,可以进行登录,相当于第三方网站在GitHub里面注册了一个应用号.这时候它说需要你去认证这个应用,这个应用是什么名字,是谁来编写的,它需要去获取你的哪些账号信息,点击认证然后就会跳转回第三方网站,这就完成了一个`OAUTH`认证.

具体流程:

```sequence
APP->GitHub:跳转页面  client_id, scope
GitHub->APP:code/ticket
Note right of GitHub:用户确认
APP->GitHub:POST 获取access_token
GitHub->APP:access_token
Note right of GitHub:需要认证的资源
APP->GitHub:GET 获取资源
GitHub->APP:response
```

第一步:比如codewar这个app,它需要在GitHub上注册一个app编号,就是client_id,然后它会直接跳转到GitHub上,让用户去确认认证信息,这时候它会把`client_id`带上,以及这个app想要获取的scope信息是什么.这时候用户进行确认,比如点`authorize`,这时候它就给app同步跳转了一个叫`code/ticket`,就相当于一个单据,这个单据是GitHub发放的.

接下来app就拿到这个code和单据,就会去获取一个`access_token`,拿到这个`access_token`请求后,GitHub就给它返回了一个`access_token`.这个时候codewars这个app永远不知道GitHub上的账户名和密码,对它来说是透明的.这个`access_token`也好,`code/ticket`也好,都是GitHub自己去建立的一种机制和自己内部的权限机制.

用`access_token`去获取资源,GitHub就有个验证,这个`access_token`的scope的范围是否能够让它去获取这个资源:如果可以的话就把response给它;如果不行的话,会返回一个forbidden,你的scope已经越界了.

因为OAUTH是需要你去申请一个`app_id`,但是其实我们也可以通过一个最简单的方式,我们看最底层方式:在GitHub主页里面有一个`settings`->`personal access tokens`, 可以生成一个新的token,可以填写`token`的描述,还可以限定获取哪些资源,这个时候就描述清楚这个`token`的`scope`, 然后生成这个`token`.生成了一串看起来像`uuid`的东西.

此时,在应用程序这一端:写一个基本的OAUTH.

`headers`里面放了一个,跟刚才基本认证一样,放了一个`Authorization`,它里面最开始的时候,基本认证的时候是叫`Basic`,后面是一个`base64`的账户名和密码的一个串.这时候我们就放一个`token`.

此时我们想去获取一下`user/emails`信息,首先给一个`response`,也是`requests`发出去的,construct一个URL,URL就是我这个user的emails信息`'user/emails'`,`headers`就把`headers`自己带上,这就完成了认证的过程.因为这个`token`是我们直接从网站上copy下来的,按正常流程,如果有一个应用,它首先要和GitHub做两次交互获得`access_token`,现在是完成的最后一步.

```python
def basic_oauth():
    headers = {'Authorization': 'token ff43fb7d15250964cf13d2d0ff4f8fd648ff3bb2'}
    response = requests.get(construct_url('user/emails'), headers=headers)
    print(response.request.headers)
    print(response.text)
    print(response.status_code)
    
basic_oauth()
```

现在打印一下`response.request.headers`是什么,以及`response`的结果是什么,最后再看看`resp`的状态码.

简单运行一下这个文件, 此时我们相当于用`token`的方式,`token`上什么也没有,token上就是一串码,还是GitHub自己管理的,它不能用b64来解析出账户名和密码.这时候`headers`把`Authroriazion`带上,就正常获得了信息.如果不加认证的话信息是获取不到的.

![image-20200210175730165](/Users/gregoryshen/Library/Application Support/typora-user-images/image-20200210175730165.png)

试一下不加`headers`:

![image-20200210175815298](/Users/gregoryshen/Library/Application Support/typora-user-images/image-20200210175815298.png)

此时是获取不到这个信息的,是401

我们其实还有更好的方法,因为每次写认证都要写一个`headers`,比如下次`get`什么请求都要写`headers`.`requests`库给大家提供了一个很好的语法糖,它在里面自己封装了一个叫做`requests.auth`,它的auth都是继承自`AuthBase`,无非就是auth在`headers`上加点东西.比如说专门给GitHub写一个它独特的认证的头:这里面要实现两个方法,第一个`__init__`,我是想提供`token`的,`token`是什么呢,首先要初始化一个;接下来要实现一个`__call__`方法,这时候传给它一个`request`,在`request`的`headers`里加`Authorization`信息:首先是一个`token`,那就是两个东西join在一起,中间是个空格,第二块就是刚传进来的token的信息:`self.token`,然后把`request`再传回去

```python
from requests.auth import AuthBase

class GithubAuth(AuthBase):
  
    def __init(self, token):
        self.token = token
        
    def __call__(self, r):
        # request 加headers
        r.headers['Authorization'] = ' '.join(['token', self.token])
        return r
```

此时上面的写法就可以改变一下了:我们现在编一个叫`oauth_advance`的小方法

`auth`就可以用面向对象的方式改进一下,这样复用性比较强,我们把刚才的token再次传递进去,这时候`response`的写法就变得简单了,(变成了和基本认证写法差不多的

![截屏2020-02-1018.23.15](/Users/gregoryshen/Desktop/截屏2020-02-1018.23.15.png)

简单回顾一下,这就是我们的一个`OAUTH`认证,它是建立在client端和GitHub平台之间的一种认证体系,它相对于基本认证来说更加安全,因为它没有直接把明文传输,而它是让需要GitHub平台进行确认的,app完全是没有拿到用户名密码,所以不容易去暴露用户的隐私,它也是很好的一种`HTTP`认证的模式.

### 5-2 Proxy代理

在网络请求中,我们首先只是和中介打交道,在内网中`laptop`和`proxy`打交道,此时`laptop`就是一个客户端,中间人充当了一个服务端角色,中间人其实是把这个请求拿下来,然后它再和外部的服务器打交道,对于后面这一段,代理就相当于是一个客户端,服务器就相当于是一个服务端,此时就完成了一个代理工作.

代理中可以完成的协议有很多,主要的工作就是把请求转发出去,可以通过各种各样的模式进行转发,它一个常用的应用就是如何去跳过防火墙访问外网.

通过requests库也可以帮大家实现这样一个代理,

1. 启动代理服务Heroku

   ​	  Heroku类似中国的阿里云

2. 在主机1080端口启动Socks服务

3. 将请求转发到1080端口

4. 获取相应资源

代码实现:

首先需要安装`Requests`库对于`socksv5`的一个支持: `pip install 'requests[socks]'`

此时利用`Requests`库,首先要定义一系列的`proxies`,`proxies`一般定义出来就是对于所有的HTTP请求要走哪个协议(比如说走`socks5`的协议,`socks5`也是一个最早的时候一种类似于HTTP的一个协议,在会话层),对于HTTPS的请求也一样,也把它转到`socks5`本机的1080端口.

给一个不能直接访问的URL,然后用`Requests`去访问,得到`timeout`的结果 

```python
>>> import requests
>>> proxies = {'http': 'socks5://127.0.0.1:1086', 'https': 'socks5://127.0.0.1:1086'}
>>> url = 'https://www.facebook.com'
>>> response = requests.get(url, timeout=10)
```

![截屏2020-02-1118.16.32](/Users/gregoryshen/Desktop/截屏2020-02-1118.16.32.png)

![截屏2020-02-1118.17.23](/Users/gregoryshen/Desktop/截屏2020-02-1118.17.23.png)

这时候加一个`proxies`,再去请求一下,

```python
>>> resp = requests.get(url, proxies=proxies, timeout=10)
>>> resp.status_code
200
```

![截屏2020-02-1322.53.48](/Users/gregoryshen/Desktop/截屏2020-02-1322.53.48.png)

其实这个原理也就很简单,我就启动了一个代理服务器,把我本机所有的请求发过去,然后可以让那些我触及不到的请求过来,这时候就相当于用了一个绕过防火墙.其实内网和外网也可以这样使用,只不过更加进阶一点.

### 5-3 Session和Cookie

HTTP是一种无状态的响应,就是一个请求过去,和下一个请求没有任何关系.但是经常有很多应用需要让两个有关系,比如你已经是个登录用户了,你现在已经把一些东西加入到购物车,那不能说跳转个页面购物车东西没了,因为你是没有状态的,所以这时候需要两种机制来解决:一个是session一个是cookie

session位于服务器端来存储一些用户信息,去保留这种状态;cookie是浏览器端来存储

首先来看看cookie的存储原理:

1. 浏览器首先发送一个HTTP请求(无cookie),它是第一个请求所以没有任何cookie,











