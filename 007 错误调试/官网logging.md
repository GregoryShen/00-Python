# [Logging HOWTO](https://docs.python.org/3.8/howto/logging.html#logging-howto)

## Basic Logging Tutorial

Logging is a means of tracking events that happen when some software runs. The software’s developer adds logging calls to their code to indicate that certain events have occurred. An event is described by a descriptive message <u>which can optionally contain ==variable data==</u> (==i.e. data that is potentially different for each occurrence of the event==). Events also have an importance which the developer ascribes to the event; the importance can also be called the level or severity.

### When to use logging

Logging provides a set of convenience functions for simple logging usage. These are `debug()`, `info()`, `warning()`, `error()` and `critical()`. To determine when to use logging, see the table below, which states, for each of a set of common tasks, the best tool to use for it.

| Task you want to perform                                     | The best tool for the task                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Display console output for ordinary usage of a command line script or program | `print()`                                                    |
| Report events that **occur during normal operation** of a program (e.g. for **<u>status monitoring</u>** or <u>**fault investigation**</u>) | `logging.info()` (or `logging.debug()` for very detailed output for diagnostic purposes) |
| <u>Issue a warning</u> regarding a particular runtime event  | `warnings.warn()` in library code ==if the issue is <u>avoidable</u> and the <u>client application should be modified to eliminate the warning</u>==<br>`logging.warning()` ==if <u>there is nothing the client application can do about the situation</u>, but the event should still be noted== |
| <u>Report an error</u> regarding a particular runtime event  | Raise an exception                                           |
| <u>Report suppression of an error</u> **without raising an exception** (e.g. <u>error handler</u> in a long-running server process) | `logging.error()`, `logging.exception()` or `logging.critical()` as appropriate for <u>the specific error</u> and <u>application domain</u> |

The logging functions are named after the level or severity of the events they are used to track. The standard levels and their applicability are described below(in increasing order of severity):

| Level      | When it’s used                                               |
| ---------- | ------------------------------------------------------------ |
| `DEBUG`    | Detailed information, typically of interest only when diagnosing problems. |
| `INFO`     | Confirmation that things are working as expected.            |
| `WARNING`  | An indication that something unexpected happened, or indicative of **some problem in the near future** (e.g. ‘disk space low’). <u>The software is ==still working as expected==.</u> |
| `ERROR`    | Due to a more serious problem, the software has ==not been able to perform some function==. |
| `CRITICAL` | A serious error, indicating that the program itself may be ==unable to continue running==. |

**<u>The default level is `WARNING`</u>**, which means that only events of this level and above will be tracked, unless the logging package is configured to do otherwise.

Events that are tracked can be handled in different ways. The simplest way of handling tracked events is to print them to the console. Another common way is to write them to a disk file.

### A simple example

A very simple example is:

```python
import logging
logging.warning('Watch out!')	# will print a message to the console
logging.info('I told you so')	# will not print anything
```

If you type these lines into a script and run it, you’ll see:

```python
WARNING:root:Watch out!
```

printed out on the console. The `INFO` message doesn’t appear because the default level is `WARNING`. The printed message includes the indication of the level and the description of the event provided in the logging call, i.e. ‘Watch out!’. Don’t worry about the ‘root’ part for now: it will be explained later. The acutal output can be formatted quite flexibly if you need that; formatting options will also be explained later.

### Logging to a file

A very common situation is that of recording logging events in a file, so let’s look at that next. Be sure to try  the following in a newly-started Python interpreter, and don’t just continue from the session described above:

```python
import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
```



### Logging from multiple modules



### Logging variable data



### Changing the format of displayed messages



### Displaying the date/time in messages



### Next Steps



## Advanced Logging Tutorial

Logging Levels

useful Handlers

Exceptions raised during logging

Using arbitrary objects as messages

Optimization