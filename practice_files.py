Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
list(range(25,50,5))
[25, 30, 35, 40, 45]
list(range(50,25,-5))
[50, 45, 40, 35, 30]
a={1:'xyz',2:'pqr',3:'uvw'}
type(a)
<class 'dict'>
print(a[3])
uvw
b={True:'456',None:78.96,[4,5,6]:{'ghi':10}}
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    b={True:'456',None:78.96,[4,5,6]:{'ghi':10}}
TypeError: unhashable type: 'list'
b={True:'456',{'ghi':10}:[4,5,6],None:76.23}
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    b={True:'456',{'ghi':10}:[4,5,6],None:76.23}
TypeError: unhashable type: 'dict'
b={True:[4,5,6],None:'abc',50:{'abc':10.34}}
b={True:[4,5,6],None:'abc',50:{'abc':10.34}}
print(b[None])
abc
type(b)
<class 'dict'>
x=15
y=20
print(x+y)
35
print(y-x)
5
print(x*y)
300
print(y/x)
1.3333333333333333
print(y//x)
1
print(30**3)
27000
m=100
n=400
print(m/n)*100
0.25
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print(m/n)*100
TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
print((m/n)*100)
25.0
25.0
25.0
r=6
r+=4
print(r)
10
r-=2
print(r)
8
r*=10
print(r)
80
r/=3
print(r)
26.666666666666668
m=50
n=30
print(m>n)
True
print(n<m)
True
print(m<n)
False
x=200
y=100
z=50
print(x>=y)
True
print(x>=z)
True
print(y>=z)
True
print(x<=y)
False
>>> print(x<=z)
False
>>> print(y<=z)
False
>>> print(x!=y)
True
>>> print(x==y)
False
>>> p=False
>>> q=False
>>> print(p and q)
False
>>> print(p or q)
False
>>> a=True
>>> b=True
>>> print(a and b)
True
>>> print(a or b)
True
>>> r=True
>>> s=False
>>> print(r and s)
False
>>> print(r or s)
True
>>> u=False
>>> v=True
>>> print(u and v)
False
>>> print(u or v)
True
>>> print(not u)
True
>>> print(not v)
False
>>> print('HI'+'ALL')
HIALL
>>> print('HI'*3)
HIHIHI
