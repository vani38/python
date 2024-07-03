Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
list(range(50,25,5))
[]
range(50)
range(0, 50)
list(range(50,25,5))
[]
range(25,50,5)
range(25, 50, 5)
list(range(25,50,5))
[25, 30, 35, 40, 45]
range(50,25,-5)
range(50, 25, -5)
list(range(50,25,-5))
[50, 45, 40, 35, 30]
a={x:'xyz',y:'pqr',z:'uvw'}
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a={x:'xyz',y:'pqr',z:'uvw'}
NameError: name 'x' is not defined
a={1:'xyz',2:'pqr',3:'uvw'}
type(a)
<class 'dict'>
a(2)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a(2)
TypeError: 'dict' object is not callable
print(a[2])
pqr
b={True:'abc',None:10,{'mnop':4.5}:'name'}
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    b={True:'abc',None:10,{'mnop':4.5}:'name'}
TypeError: unhashable type: 'dict'
>>> b={None:'abc',True:[4,5,6],9.8:{'efg':40}}
>>> type(b)
<class 'dict'>
>>> print(b[9.8])
{'efg': 40}
>>> x=10
>>> y=15
>>> z=x+y
>>> print(z)
25
>>> print(x+y)
25
>>> a=50
>>> b=10
>>> print(a-b)
40
>>> print(x*y)
150
>>> print(a/b)
5.0
>>> print(y//x)
1
>>> print(%(a))
SyntaxError: invalid syntax
>>> print(a%)
SyntaxError: invalid syntax
>>> a=10
>>> print(a**)
SyntaxError: invalid syntax
>>> print(10**)
SyntaxError: invalid syntax
>>> print(10**2)
100
>>> print(10**3)
1000
>>> print(25**4)
390625
a=100
b=300
print((a/b)*100)


      
