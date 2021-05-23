https://docs.python.org/zh-cn/3/using/cmdline.html#environment-variables

这些环境变量会影响Python的行为,它们是在命令行开关之前被处理的, 但-E或-l除外.根据约定, 当存在冲突时命令行开关会覆盖环境变量的设置

PYTHONHOME

​	  更改标准Python库的位置. 默认情况下库是在 `prefix/lib/pythonversion`和`exec_prefix/lib/pythonversion`中搜索, 其中`prefix`和`exec_prefix`是由安装位置确定的目录, 默认都位于`/usr/local`

当`PYTHONHOME`被设为单个目录时, 它的值会同时替代`prefix`和`exec_prefix`, 要为两者指定不同的值, 请将`PYTHONHOME`设为`prefix:exec_prefix`

PYTHONPATH

​	增加模块文件默认搜索路径.所用格式与终端PATH相同: 一个或多个由`os.pathsep`分隔的目录路径名称(例如Unix上用冒号而在Windows上用分号). 默认忽略不存在的目录.

除了普通目录之外, 单个PYTHONPATH 条目可以引用包含纯Python模块的zip文件(源代码或编译形式).无法从zip文件导入扩展模块

默认索引路径依赖于安装路径,但通常都是以`prefix/lib/pythonversion`开始, 它总是会被添加到PYTHONPATH

有一个附加目录将被插入到索引路径的PYTHONPATH之前, 正如上文中接口选项所描述的. 搜索路径可以在Python程序内作为变量`sys.path`来进行操作

​	Augment the default search path for module files. The format is the same as the shell’s PATH: one or more directory  pathnames separated by os.pathsep (e.g. colons on Unix or semicolons on Windows). Non-existent directories are silently ignored.

In addition to normal directories, individual PYTHONPATH entries may refer to zipfiles containing pure Python modules(in either source or compiles form). Extension modules cannot be imported from zipfiles.

The default search path is installation dependent, but generally begins with `prefix/lib/pythonversion`. It is always appended to PYTHONPATH.

An additional directory will be inserted in the search path in front of PYTHONPATH as described above under Interface options. The search path can be manipulated from within a Python program as the variable `sys.path`

#### sys.path

一个由字符串组成的列表,用于指定模块的搜索路径.初始化自环境变量PYTHONPATH, 再加上一条与安装有关的默认路径.

程序启动时将初始化该列表, 列表的第一项`path[0]`目录含有调用Python解释器的脚本. 如果脚本目录不可用(比如以交互方式调用解释器, 或脚本是从标准输入中读取的), 则`path[0]`为空字符串, 这将导致Python 优先搜索当前目录中的模块. 注意,脚本目录将插入在PYTHONPATH的条目之前

程序可以随意修改本列表用于自己的目的. 只能向`sys.path`中添加`string`和`bytes`类型, 其他数据类型将在导入期间被忽略.

A list of strings that specifies the search path for modules. Initialized from the environment variable PYTHONPATH, plus an installation-dependent default.

As initialized upon program startup, the first item of this list, `path[0]`, is the directory containing the script that was used to invoke the Python interpreter. If the script directory is not available (e.g. if the interpreter is invoked interactively or if the script is read from standard input), `path[0]`is the empty string, which directs Python to search modules in the current directory first. Notice that the script directory is inserted before the entries inserted as a result of PYTHONPATH.

A program is free to modify this list for its own purposes. Only strings and bytes should be added to `sys.path`; all other data types are ignored during import.

