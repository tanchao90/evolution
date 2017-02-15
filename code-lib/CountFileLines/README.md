
# 统计文件行数

## 功能
- 指定目录，统计该目录下所有文件总行数
- 需要指定被统计的的文件类型
- 支持目录过滤

## Example
```python
path = "C:\Users\\username\Desktop\\tt"
fileTypes = ['.py']
ignoreDirs = ['.git']

count, details = countFileLines(path, fileTypes, ignoreDirs)

print '## line count:', count

for filename, cnt in details.iteritems():
    print '  ', filename, cnt
```