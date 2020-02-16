1. 请使用`try…finally`正确关闭文件资源

```python
try:
    f = open('/path/to/file', 'r')
    f.read()
finally:
    if f:
        f.close()
```

1. adfadfa
2. 