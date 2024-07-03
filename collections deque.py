Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from collections import deque
>>> d=deque([1,2,3,4,5])
>>> d.append(6)
>>> print(d)
deque([1, 2, 3, 4, 5, 6])
>>> d.appendleft(0)
>>> print(d)
deque([0, 1, 2, 3, 4, 5, 6])
>>> d.pop()
6
>>> d.popleft()
0
>>> d.extend[7,8,9]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    d.extend[7,8,9]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> d.extend([7,8,9])
>>> print(d)
deque([1, 2, 3, 4, 5, 7, 8, 9])
>>> d.extendleft([0,-1,-2])
>>> print(d)
deque([-2, -1, 0, 1, 2, 3, 4, 5, 7, 8, 9])
>>> d.rotate(1)
>>> print(d)
deque([9, -2, -1, 0, 1, 2, 3, 4, 5, 7, 8])
>>> d.rotate(-1)
>>> print(d)
deque([-2, -1, 0, 1, 2, 3, 4, 5, 7, 8, 9])
>>> d.rotate(-1)
print(d)
deque([-1, 0, 1, 2, 3, 4, 5, 7, 8, 9, -2])
print(len(d))
11
print(d[0])
-1
print(d[3])
2
d.remove(3)
print(d)
deque([-1, 0, 1, 2, 4, 5, 7, 8, 9, -2])
d.clear()
print(d)
deque([])
