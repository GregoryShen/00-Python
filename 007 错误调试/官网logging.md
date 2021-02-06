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

And now if we open the file and look at what we have, we should find the log messages:

```bash
DEBUG:root:This message should go to the log file
INFO:root:So should this
WARNING:root:And this, too
```

This example also shows how you can set the logging level which acts as the threshold for tracking. In this case, because we set the threshold to `DEBUG`, all of the messages were printed.

If you want to set the logging level from a command-line option such as:

```tex
--log=INFO
```

and you have the value of the parameter passed for `--log` in some variable loglevel, you can use:

```python
getattr(logging, loglevel.upper())
```

to get the value which you’ll pass `basicConfig()` via the level argument. You may want to error check any user input value, perhaps as in the following example:

```python
# assuming loglevel is bound to the string value obtained from the 
# command line argument. Convert to upper canse to allow the user to
# specify --log=DEBUG or --log=debug
numeric_level = getattr(logging, loglevel.upper(), None)
if not isinstance(numeric_level, int):
    raise ValueError('Invalid log level: {}'.format(loglevel))
logging.basicConfig(level=numeric_level, ...)
```

The call to `basicConfig()` should come before any calls to debug(), info() etc. As it’s intended as a one-off simple configuration facility, only the first call will actually do anything: subsequent calls are effectively no-ops.

If you run the above script several times, the messages from successive runs are appended to the file `*example.log*`. ==If you want each run to start afresh, not remembering the messages from earlier runs, you can specify the *filemode* argument==, by changing the call in the above example to:

```python
logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)
```

The output will be the same as before, but the log file is no longer appended to, so the messages from earlier runs are lost.

### Logging from multiple modules

```python
# myapp.py
import logging
import mylib

def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logging.info('Started')
    mylib.do_someting()
    logging.info('Finished')
    
if __name__ == '__main__':
    main()
    
# mylib.py
import logging

def do_something():
    logging.info('Doing something')
```

If you run `myapp.py`, you should see this in `myapp.log`:

```bash
INFO:root:Started
INFO:root:Doing something
INFO:root:Finished
```

which is hopefully what you were expecting to see. You can generalize this to multiple modules, using the pattern in `mylib.py`. Note that for this simple usage pattern, you won’t know, by looking in the log file, where in your application your messages came from , apart from looking at the event description. If you want to track the location of your messages, you’ll need to refer to the documentation beyond the tutorial level.

### Logging variable data

To log variable data, use a format string for the event description message and append the variable data as arguments. For example:

```python
import logging
logging.warning('%s before you %s', 'Look', 'leap!')
```

will display:

```bash
WARNING:root:Look before you leap!
```

As you can see, merging of variable data into the event description message uses the old, %-style of string formatting. This is for backwards compatibility: the logging package pre-dates newer formatting options such as `str.format()` and `string.Template`. These newer formatting options are supported, but exploring them is outside the scope of this tutorial: see <u>Using particular formatting styles throughout your application</u> for more information.

### Changing the format of displayed messages

To change the format which is used to display messages, you need to specify the format you want to use:

```python
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')
```

which would print:

```python
DEBUG:This message should appear on the console
INFO:So should this
WARNING:And this, too
```

Notice that the ‘root’ which appeared in earlier examples has disappeared. For a full set of things that can appear in format strings, you can refer to the documentation for <u>LogRecord attributes</u>, but for simple usage,  you just need the levelname(severity), message(event description, including variable data) and perhaps to display when the event occurred. This is described in the next section.

### Displaying the date/time in messages

To display the date and time of an event, you would place ‘%(asctime)s’ in your format string:

```python
import logging
logging.basicConfig(format='%(asctime)s %(message)s')
logging.warning('is when this event was logged.')
```

which should print something like this:

```bash
2010-12-12 11:41:42,612 is when this event was logged.
```

The default format for date/time display (shown above) is like ISO8601 or RFC 3339. If you need more control over the formatting of the date/time, provide a `datefmt` argument to `basicConfig`, as in this example:

```python
import logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.warning('is when this event was logged.')
```

which would display something like this:

```bash
12/12/2010 11:46:36 AM is when this event was logged.
```

The format of the `datefmt` argument is the same as supported by `time.strftime()`

### Next Steps

略

## Advanced Logging Tutorial

The logging library takes a modular approach and offers several categories of components: loggers, handlers, filters and formatters.

* Loggers expose the interface that application code directly uses.
* Handlers send the log records (created by loggers) to the appropriate destination.
* Filters provide a finer grained facility for determining which log records to output.
* Formatters specify the layout of log records in the final output.

Log event information is passed between loggers, handlers, filters and formatters in a `LogRecord` instance.

Logging is performed by calling methods on instances of the Logger class (hereafter called loggers). Each instance has a name, and they are conceptually arranged in a namespace hierarchy using dots (periods) as separators. For example, a logger named ‘scan’ is the parent of loggers ‘`scan.text`’, ‘`scan.html`’ and ‘`scan.pdf`’. Logger names can be anything you want, and indicate the area of an application in which a logged message originates.

A good convention to use when naming loggers is to use a module-level logger, in each module which uses logging, named as follows:

```python
logger = logging.getLogger(__name__)
```

This means that logger names track the package/module hierarchy, and it’s intuitively obvious where events are logged just from the logger name.

The root of the hierarchy of loggers is called the root logger. That’s the logger used by the functions debug(), info(), warning(), error() and critical(), which just call the same-named method of the root logger. The functions and the methods have the same signatures. The root logger’s name is printed as ‘root’ in the logged output.

It is, of course, possible to log messages to different destinations. Support is included in the package for writing log messages to files, HTTP GET/POST locations, email via SMTP, generic sockets, queues, or OS-specific logging mechanisms such as syslog or the Windows NT event log. Destinations are served by handler classes. You can create your own log destination class if you have special requirements not met by any of the built-in handler classes.

By default, no destination is set for any logging messages. You can specify a destination (such as console or file) by using `basicConfig()` as in the tutorial examples. If you call the functions debug(), info(), warning(), error() and critical(), they will check to see if no destination is set; and if one is not set, they will set a destination of the console (`sys.stderr`) and a default format for the displayed message before delegating to the root logger to do the actual message output.

The default format set by `basicConfig()` for message is:

```python
severity:logger name:message
```

You can change this by passing a format string to `basicConfig()` with the format keyword argument. For all options regarding how a format string is constructed, see Formatter Objects.

### Logging Flow

The flow of log event information in loggers and handlers is illustrated in the following diagram.

![](https://docs.python.org/3.8/_images/logging_flow.png)

### Loggers

Logger objects have a threefold job. First, they expose several methods to application code so that applications can log messages at runtime. Second, logger objects determine which log messages to act upon based upon severity (the default filtering facility) or filter objects. Third, logger objects pass along relevant log messages to all interested log handlers.

The most widely used methods on logger objects fall into two categories: configuration and message sending.

These are the most common configuration methods:

* `Logger.setLevel()` specifies the lowest-severity log message a logger will handle, where debug is the lowest built-in severity level and critical is the highest built-in severity. For example, if the severity level is INFO, the logger will handle only INFO, WARNING, ERROR, and CRITICAL messages and will ignore DEBUG messages.
* `Logger.addHandler()` and `Logger.removeHandler()` add and remove handler objects from the logger object. 
* `Logger.addFilter()` and `Logger.removeFilter()` add and remove filter objects from the logger object.

You don’t need to always call these methods on every logger you create. See the last two paragraphs in this section.

With the logger object configured, the following methods create log messages:

* `Logger.debug()`, `Logger.info()`, `Logger.warning()`, `Logger.error()`, and `Logger.critical()` all create log records with a message and a level that corresponds to their respective method names. The message is actually a format string, which may contain the standard string substitution syntax of ‘%s’, ‘%d’, ‘%f’, and so on. The rest of their arguments is a list of objects that correspond with the substitution fields in the message. With regard to `**kwargs`, the logging methods care only about a keyword of `exc_info` and use it to determine whether to log exception information.
* `Logger.exception()` creates a log message similar to `Logger.error()`. The difference is that `Logger.exception()` dumps a stack trace along with it. Call this method only from an exception handler.
* `Logger.log()` takes a log level as an explicit argument. This is a little more verbose for logging messages than using the log level convenience methods listed above, but this is how to log at custom log levels.

==`getLogger()` returns a reference to a logger instance with the specified name if it is provided, or `root` if not.== The names are period-separated hierarchical structures. <u>Multiple calls to `getLogger()` with the same name will return a reference to the same logger object.</u> Loggers that are further down in the hierarchical list are children of loggers higher up in the list. 

Loggers have a concept of <u>effective level</u>. If a level is not explicitly set on a logger, the level of its parent is used instead as its effective level. If the parent has no explicit level set, its parent is examined, ans so on - all ancestors are searched until an explicitly set level is found. The root logger always has an explicit level set (WARNING by default). When deciding whether to process an event, the effective level of the logger is used to determine whether the event is passed to the logger’s handlers.

<u>**Child loggers propagate[^1] messages up to the handlers associated with their ancestor loggers.**</u> Because of this, it is <u>unnecessary to define and configure handlers for all the loggers</u> an application uses. It is sufficient to configure handlers for a top-level logger and create child loggers as needed. (You can, however, turn off propagation by setting the propagate attribute of a logger to False.)

### Handlers

Handler objects are responsible for dispatching the appropriate log messages (based on the log messages’ severity) to the handler’s specified destination. Logger objects can add zero or more handler objects to themselves with an `addHandler()` method. As an example scenario, an application may want to send all log messages to a log file, all log messages of error or higher to stdout, and all messages of critical to an email address. This scenario requires three individual handlers where each handler is responsible for sending messages of a specific severity to a specific location.

The standard library includes quite a few handler types ; the tutorials use mainly `StreamHandler` and `FileHandler` in its examples.

There are very few methods in a handler for application developers to concern themselves with. The only handler methods that seem relevant for application developers who are using the built-in handler objects(that is, not creating custom handlers) are the following configuration methods:

* The `setLevel()` method, just as in logger objects, specifies the lowest severity that will be dispatched to the appropriate destination. <u>*Why are there two `setLevel()` methods?* The level set in the **logger determines which severity of messages it will pass to its handlers**. The level set in each **handler determines which messages that handler will send on**.</u>
* `setFormatter()` selects a Formatter object for this handler to use.
* `addFilter()` and `removeFilter()` respectively configure and deconfigure filter objects on handlers.

<u>Application code should not directly instantiate and use instances of Handler.</u> Instead, the Handler class is a base class that defines the interface that all handlers should have and establishes some default behavior that child classes can use (or override).

### Formatters

Formatter objects configure the final order, structure, and contents of the log message. Unlike the base `logging.Handler` class, application code may instantiate formatter classes, although you could likely subclass the formatter if your application needs special behavior. <u>The constructor takes three optional arguments - **a message format string**, **a date format string** and **a style indicator.**</u>

```python
logging.Formatter.__init__(fmt=None, datafmt=None, style='%')
```

If there is no message format string,  the default is to use the raw message. If there is no date format string, the default date format is:

```shell
%Y-%m-%d %H:%M:%S
```

with the milliseconds tacked on at the end. The style is one of `%`, `{`, or `$`。 If one of these is not specified, then `%` will be used.

If the style is `%`, the message format string uses `%(<dictionary key>)s` styled string substitution; the possible keys are documented in LogRecord attributes. If the style is `{`, the message format string is assumed to be compatible with `str.format()` (using keyword arguments), while if the style is `$` then the message format string should conform to what is expected by `string.Template.substitute()`.

The following message format string will log the time in a human-readable format, the severity of the message, and the contents of the message, in that order:

```shell
'%(asctime)s - %(levelname)s - %(message)s'
```

Formatters use a user-configurable function to convert the creation time of a record to a tuple. By default, `time.localtime()` is used; to change this for a particular formatter instance, set the `converter` attribute of the instance to a function with the same signature as `time.localtime()` or `time.gmtime()`. To change it for all formatters, for example if you want all logging times to be shown in GMT, set the converter attribute in the Formatter class(to `time.gmtime` for GMT display)

### Configuring Logging

Programmers can configure logging in three ways:

1. Creating loggers, handlers, and formatters explicitly using Python code that calls the configuration methods listed above.
2. Creating a logging config file and reading it using `fileConfig()` function.
3. Creating a dictionary of configuration information and passing it to the `dictConfig()` function.

For the reference documentation on the last two options, see Configuration functions. The following example configures a very simple logger, a console handler, and a simple formatter using Python code:

```python
import logging

# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter 这里第二个参数name指的是logger的name
formatter = logging.Formatter('%(asctime)s - %(name)s- %(levelname)s- %(message)s')

# add formatter to ch
ch.addFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
```

Running this module from the command line produces the following output:

```shell
$ python simple_logging_module.py
2005-03-19 15:10:26,618 - simple_example - DEBUG - debug message
2005-03-19 15:10:26,620 - simple_example - INFO - info message
2005-03-19 15:10:26,695 - simple_example - WARNING - warn message
2005-03-19 15:10:26,697 - simple_example - ERROR - error message
2005-03-19 15:10:26,773 - simple_example - CRITICAL - critical message
```

The following Python module creates a logger, handler and formatter nearly identical to those in the example listed above, with the only difference being the names of the objects:

```python
import logging
import logging.config

logging.config.fileConfig('logging.conf')

# create logger
logger = logging.getLogger('simpleExample')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
```

Here is the `logging.conf` file:

```ini
[loggers]
keys=root,simpleExample

[handlers]
keys=consoleHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler

[logger_simpleExample]
level=DEBUG
handlers=consoleHandler
qualname=simpleExample
propagate=0

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=simpleFormatter
args=(sys.stdout,)

[formatter_simpleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
datefmt=
```

The output is nearly identical to that of the non-config-file-based example:

```shell
$ python simple_logging_config.py
2005-03-19 15:38:55,977 - simpleExample - DEBUG - debug message
2005-03-19 15:38:55,979 - simpleExample - INFO - info message
2005-03-19 15:38:56,054 - simpleExample - WARNING - warn message
2005-03-19 15:38:56,055 - simpleExample - ERROR - error message
2005-03-19 15:38:56,130 - simpleExample - CRITICAL - critical message
```

You can see that the config file approach has a few advantages over the Python code approach, mainly separation of configuration and code and the ability of noncoders to easily modify the logging properties.

> Warning: The `fileConfig()`  function takes a default parameter, `disable_existing_loggers`, which defaults to `True` for reasons of backward compatibility. This may or may not be what you want, since it will cause any non-root loggers existing before the `fileConfig()` call to be disabled unless they (or an ancestor) are explicitly named in the configuration. Please refer to the reference documentation for more information, and specify `False` for this parameter if you wish.
>
> The dictionary passed to `dictConfig()` can also specify a Boolean value with key `disable_existing_loggers`, which if not specified explicitly in the dictionary also defaults to being interpreted as `True`. This leads to the logger-disabling behavior described above, which may not be what you want - in which case, provide the key explicitly with a value of `False`.

Note that the class names referenced in config files need to be either relative to the logging module, or absolute values which can be resolved using normal import mechanisms. Thus, you could use either `WatchedFileHandler` (relative to the logging module) or `mypackage.mymodule.MyHandler` (for a class defined in package `mypackage` and module `mymodule`, where `mypackage` is available on the Python import path).

In Python 3.2, a new means of configuring logging has been introduced, using dictionaries to hold configuration information. This provides a superset of the functionality of the config-file-based approach outlined above, and is the recommended configuration method for new applications and deployments. Because a Python dictionary is used to hold configuration information, and since you can populate[^2] that dictionary using different means, you have more options for configuration. For example, you can use a configuration file in JSON format, or, if you have access to YAML processing functionality, a file in YAML format, to populate the configuration dictionary. Or, of course, you can construct the dictionary in Python code, receive it in pickled form over a socket, or use whatever approach makes sense for your application.

Here’s an example of the same configuration as above, in YAML format for the new dictionary-based approach:

```yaml
version: 1
formatters:
  simple:
    format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
handlers:
  console:
    class: logging.StreamHandler
    level: DEBUG
    formatter: simple
    stream: ext://sys.stdout
loggers:
  simpleExample:
    level: DEBUG
    handlers: [console]
    propagate: no
root:
  level: DEBUG
  handlers: [console]
```

### What happens if no configuration is provided

If no logging configuration is provided, it is possible to have a situation where a logging event needs to be output, but no handlers can be found to output the event. The behavior of the logging package in these circumstances is dependent on the Python version.

For versions of Python prior to 3.2, the behavior is as follows:

* If `logging.raiseExceptions` is `False` (production mode), the event is silently dropped.
* If `logging.raiseExceptions` is `True` (development mode), a message ’No handlers could be found for logger X.Y.Z’ is printed once.

In Python 3.2 and later, the behavior is as follows:

* The event is output using a ‘handler of last resort’, stored in `logging.lastResort`. This internal handler is not associated with any logger, and acts like a `StreamHandler` which writes the event description message to the current value of `sys.stderr` (therefore respecting any redirections which may be in effect). No formatting is done on the message - just the bare event description message is printed. The handler’s level is set to `WARNING`, so all events at this and greater severities will be output.

To obtain the pre-3.2 behavior, `logging.lastResort` can be set to `None`.

### Configuring Logging for a Library

When developing a library which uses logging, you should take care to document how the library uses logging - for example, the names of loggers used. Some consideration also needs to be given to its logging configuraion. If the using application does not use logging, and library code makes logging calls, then (as described in the previous section) events of severity WARNING and greater will be printed to `sys.stderr`. This is regarded as the best default behavior.

If for some reason you don’t want these messages printed in the absence of any logging configuration, you can attach a do-nothing handler to the top-level logger for your library. This avoids the message being printed, since a handler will always be found for the library’s events: it just doesn’t produce any output. If the library user configures logging for application use, presumably that configuration will add some handlers, and if levels are sutiably configured then logging calls made in library code will send output to those handlers, as normal.

A do-nothing handler is included in the logging package: `NullHandler` (since Python 3.1). An instance of this handler could be added to the top-level logger of the logging namespace used by the library (if you want to prevent your library’s logged events being output to `sys.stderr` in the absence of logging configuration). If all logging by a library foo is done using loggers with names matching `foo.x`, `foo.x.y`, etc. then the code:

```python
import logging
logging.getLogger('foo').addHandler(logging.NullHandler())
```

should have the desired effect. If an organisation produces a number of libraries, then the logger name specified can be ‘orgname.foo’ rather than just ‘foo’.

> Note: It is strongly advised that you do not add any handlers other than `NullHandler` to your library’s loggers. This is because the configuration of handlers is the prerogative of the application developer who uses your library. The application developer knows their target audience and what handlers are most appropriate for their application: if you add handlers ‘under the hood’, you might will interfere with their ability to carry out unit tests and deliver logs which suit their requirements.

## Logging Levels

The numeric values of logging levels are given in the following table. These are primarily of interest if you want to define your own levels, and need them to have specific values relative to the predefined levels. If you define a level with the same numeric value, it overwrites the predefined value; the predefined name is lost.

| Level    | Numeric value |
| -------- | ------------- |
| CRITICAL | 50            |
| ERROR    | 40            |
| WARNING  | 30            |
| INFO     | 20            |
| DEBUG    | 10            |
| NOTSET   | 0             |

Levels can also be associated with loggers, being set either by the developer or through loading a saved logging configuraion. When a logging method is called on a logger, the logger compares its own level with the level associated with the method call. If the logger’s level is higher than the method call’s, no logging message is actually generated. This is the basic mechanism controlling the verbosity of logging output.

Logging messages are encoded as instances of the `LogRecord` class. When a logger decides to actually log an event, a `LogRecord` instance is created from the logging message.

Logging messages are subjected to a dispatch mechanism through the use of handlers, which are instances of subclass of the Handler class. Handlers are responsible for ensuring that a logged message (in the form of a `LogRecord`) ends up in a particualr location (or set of locations) which is useful for the target audience for that message (such as end users, support desk staff, system administrators, developers). Handlers are passed `LogRecord` instances intended for particular destinations. Each logger can have zero, one or more handlers associated with it (via the `addHandler()` method of Logger). In addition to any handlers directly associated with a logger, all handlers associated with all ancestors of the logger are called to dispatch the message (unless the propagate flag for a logger is set to a false value, at which point the passing to ancestor handlers stops).

Just as for loggers, handlers can have levels associated with them. A handler’s level acts as a filter in the same way as a logger’s level does. If a handler decides to actually dispatch an event, the `emit()` method is used to send the message to its destination. Most user-defined subclass of Handler will need to override this `emit()`.

### Custom Levels

Defining your own levels is possible, but should not be necessary, as the existing levels have been chosen on the basis of practical experience. However, if you are convinced that you need custom levels, great care should be exercised when doing this, and it is possibly a very bad idea to defind custom levels if you are developing library. That’s because if multiple library authors all define their own custom levels, there is a chance that the logging output from such multiple libraries used together will be difficult for the using developer to control and/or interpret, because a given numeric value might mean different things for different libraries.

## Useful Handlers



## Exceptions raised during logging

## Using arbitrary objects as messages

## Optimization

[^1]: verb.宣传；传播；使普及;繁殖，培植（植物）

[^2]:  填充，占据

