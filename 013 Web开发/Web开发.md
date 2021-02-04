## HTTP 协议简介

在Web应用中，服务器把网页传给浏览器，实际上就是把网页的HTML代码发送给浏览器，让浏览器显示出来。而浏览器和服务器之间的传输协议是HTTP。所以：

* HTML 是一种用来定义网页的文本，会HTML，就可以编写网页
* HTTP 是在网络上传输HTML的协议，用于浏览器和服务器的通信

开发者工具：

Elements 显示网页的结构， Network 显示浏览器和服务器的通信，我们点 Network , 确保第一个小红灯亮着，Chrome就会记录所有浏览器和服务器之间的通信：

在Network中，定位到第一条记录，点击，右侧将显示 Request Headers，点击右侧的 view source， 就可以看到浏览器发送给服务器的请求：

<img src="https://www.liaoxuefeng.com/files/attachments/950413532592512" style="zoom:75%;" />

最重要的头两行分析如下，第一行：

```html
GET / HTTP/1.1
```

`GET`表示一个读取请求，将从服务器获得网页数据， `/`表示URL的路径，URL总是以`/`开头，`/`就表示首页，最后的`HTTP/1.1`。目前HTTP协议的版本就是1.1，但是大部分服务器也支持1.0版本，主要区别在于1.1版本允许多个HTTP请求复用一个TCP连接，以加快传输速度。

从第二行开始，每一行都类似于`Xxx: abcdefg`

```html
Host: www.sina.com.cn
```

表示请求的域名是`www.sina.com.cn`。<u>**如果一台服务器有多个网站，服务器就需要通过`Host`来区分浏览器请求的是哪个网站。**</u>

继续往下找到 Response Headers， 点击 view source, 显示服务器返回的原始响应数据：

<img src="https://www.liaoxuefeng.com/files/attachments/950413553562752" style="zoom:75%;" />

HTTP响应分为Header和Body两部分（Body是可选项），我们在Network 中看到的Header最重要的几行如下：

```html
HTTP/1.1 200 OK
```

200 表示一个成功的响应， 后面的OK 是说明。失败的响应有404 Not Found：网页不存在，500 Internal Server Error：服务器内部出错等

```html
Content-Type: text/html
```

Content-Type 指示响应的内容，这里是 text/html 表示 HTML 网页。==浏览器就是靠Content-Type 来判断响应的内容是网页还是图片，是视频还是音乐。浏览器并不靠URL来判断响应的内容，所以，即使URL是http://example.com/abc.jpg，它也不一定就是图片。==

<u>**HTTP 响应的Body就是HTML源码**[^1]，当浏览器读取到新浪首页的HTML源码后，它会解析HTML，显示页面，然后，根据 HTML 里面的各种链接，再发送 HTTP 请求给新浪服务器，拿到相应的</u>图片、视频、Flash、JavaScript脚本、CSS等<u>各种资源，最终显示出一个完整的页面</u>。所以我们在 Network 下能看到很多额外的HTTP请求。

### HTTP 请求

跟踪了新浪的首页，我们来总结一下HTTP请求的流程：

* 浏览器首先向服务器发送HTTP请求，请求包括：
	* 方法： GET 还是 POST， GET 仅请求资源，POST会附带用户数据
	* 路径：/full/url/path
	* 域名：由Host头指定：`Host: www.sina.com`
	* 以及其他相关的Header
	* 如果是POST，那么请求还包括一个Body，包括用户数据
* 服务器向浏览器返回HTTP响应，响应包括：
	* 响应代码：200表示成功，3xx表示重定向，4xx表示客户端发送的请求有错误，5xx表示服务器端处理时发生了错误
	* 响应类型：由 Content-Type 指定，例如：`Content-Type: text/html;charset=utf-8` 表示响应类型是HTML文本，并且编码是utf-8， `Content-Type: image/jpeg`表示响应类型是JPEG格式的图片
	* 以及其他相关的Header
	*  通常服务器的 HTTP 响应会携带内容，也就是有一个Body，包含响应的内容，网页的HTML源码就在Body中
* 如果浏览器还需要继续向服务器请求其他资源，比如图片，就再次发出 HTTP 请求，重复步骤1、2

Web采用的HTTP协议采用了非常简单的请求-响应模式，从而大大简化了开发。当我们编写一个页面时，我们只需要在HTTP响应中把HTML发送出去，不需要考虑如何附带图片、视频等，浏览器如果需要请求图片和视频，它会发送另一个HTTP请求，因此，==一个HTTP请求只处理一个资源==。

HTTP协议同时具有极强的**扩展性**，虽然浏览器请求的是http://www.sina.com.cn/的首页，但是新浪<u>在HTML中可以链入其他服务器的资源</u>，比如`<img src="http://i1.sinaimg.cn/home/2013/1008/U8455P30DT20131008135420.png">` ,<u>从而将请求压力分散到各个服务器上</u>，并且，一个站点可以链接到其他站点，无数个站点互相链接起来，就形成了World Wide Web.

### HTTP 格式

每个HTTP请求和响应都遵循相同的格式，==一个 HTTP 包含 Header 和 Body 两部分，其中Body是可选的==。

HTTP协议是一种文本协议，所以它的格式也非常简单。 HTTP GET 请求的格式：

```html
GET /path HTTP/1.1
Header1: Value1
Header2: Value2
...
```

==每个Header一行一个，换行符是`\r\n`==

HTTP POST 请求的格式：

```html
POST /path HTTP/1.1
Header1: Value1
Header2: Value2
...

body data goes here...
```

==当遇到连续两个`\r\n`时，Header 部分结束，后面的数据全部是Body==

HTTP响应的格式：

```html
200 OK
Header1: Value1
Header2: Value2
...

body data goes here...
```

<u>**HTTP 响应如果包含body，也是通过`\r\n\r\n`来分隔的**</u>。请再次注意，==Body的数据类型由`Content-Type`头来确定==，如果是网页，Body 就是文本，如果是图片，Body 就是图片的二进制数据。

**<u>当存在Content-Encoding时，Body数据是被压缩的</u>**，最常见的压缩方式是 `gzip`，所以看到`Content-Encoding: gzip` 时，需要将Body数据先解压缩，才能得到真正的数据。压缩的目的在于减少 Body 的大小，加快网络传输。

[^1]: 当然指的只是上面这个请求的响应













