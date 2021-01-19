# [Logging HOWTO](https://docs.python.org/3.8/howto/logging.html#logging-howto)

## Basic Logging Tutorial

Logging is a means of tracking events that happen when some software runs. The software’s developer adds logging calls to their code to indicate that certain events have occurred. An event is described by a descriptive message <u>which can optionally contain ==variable data==</u> (==i.e. data that is potentially different for each occurrence of the event==). Events also have an importance which the developer ascribes to the event; the importance can also be called the level or severity.

### When to use logging

Logging provides a set of convenience functions for simple logging usage. These are debug(), info(), warning(), error() and critical(). To determine when to use logging, see the table below, which states, for each of a set of common tasks, the best tool to use for it.

| Task you want to perform | The best tool for the task |
| ------------------------ | -------------------------- |
|                          |                            |



### A simple example



### Logging to a file



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