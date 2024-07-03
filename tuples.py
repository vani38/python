Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=(100,23,45,36,76,87,90,14,21,54,68,87,19)
>>> a[0]
100
>>> a[-5]
21
>>> a[0:5:2]
(100, 45, 76)
>>> a[8:4:-3]
(21, 87)
>>> a.count(90)
1
>>> #index()
>>> a.index(87)
5
>>> #tuple assignment
>>> (a,b)=(15,25)
>>> print(a)
15
>>> print(b)
25
>>> (x,y,z)=([20,30],'Ram',7.8)
>>> print(x)
[20, 30]
>>> print(y)
Ram
>>> print(z)
7.8
>>> print(x=y)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print(x=y)
TypeError: 'x' is an invalid keyword argument for print()
>>> x=y
>>> y=z
>>> z=x
>>> print(x)
Ram
>>> print(y)
7.8
>>> print(z)
Ram
a.max()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a.max()
AttributeError: 'int' object has no attribute 'max'
a=(100,23,45,36,76,87,90,14,21,54,68,87,19)
a.max()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a.max()
AttributeError: 'tuple' object has no attribute 'max'
max(a)
100
a=(100,23,45,36,76,87,90,14,21,54,68,87,19,23,45,68,36,87,68,90)
set(a)
{100, 36, 68, 76, 45, 14, 19, 21, 87, 23, 54, 90}
 #dictionary
x={True:'manoj',None:25.0,1:[25,50]}
x.get(None)
25.0
a.get(3)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a.get(3)
AttributeError: 'tuple' object has no attribute 'get'
x.get(4)
x.get(4,'not found')
'not found'
k={'karnataka':'bangalore','andra pradesh':'amaravati','madhya pradesh':'bhopal'}
k['uttar pradesh']='lucknow'
print(k)
{'karnataka': 'bangalore', 'andra pradesh': 'amaravati', 'madhya pradesh': 'bhopal', 'uttar pradesh': 'lucknow'}
#replace
k['karnataka']='karnatak'
print(k)
{'karnataka': 'karnatak', 'andra pradesh': 'amaravati', 'madhya pradesh': 'bhopal', 'uttar pradesh': 'lucknow'}
k['karnatak']='bangalore'
print(k)
{'karnataka': 'karnatak', 'andra pradesh': 'amaravati', 'madhya pradesh': 'bhopal', 'uttar pradesh': 'lucknow', 'karnatak': 'bangalore'}
k['karnataka']='bangalore'
print(k)
{'karnataka': 'bangalore', 'andra pradesh': 'amaravati', 'madhya pradesh': 'bhopal', 'uttar pradesh': 'lucknow', 'karnatak': 'bangalore'}
del.y['lucknow']
SyntaxError: invalid syntax
del y['lucknow']
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    del y['lucknow']
TypeError: 'float' object does not support item deletion
del k['lucknow']
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    del k['lucknow']
KeyError: 'lucknow'
del k['uttar pradesh']
print(k)
{'karnataka': 'bangalore', 'andra pradesh': 'amaravati', 'madhya pradesh': 'bhopal', 'karnatak': 'bangalore'}
s={'Name':['vani','ramesh',' sachin'],['Age':29,34,28]
   
SyntaxError: invalid syntax
s={'Name':['vani','ramesh',' sachin'],['Age':[29,34,28]]
   
SyntaxError: invalid syntax
s={'Name':['vani','ramesh',' sachin'],'Age':[29,34,28]}
   
print(s)
   
{'Name': ['vani', 'ramesh', ' sachin'], 'Age': [29, 34, 28]}
s.key()
   
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    s.key()
AttributeError: 'dict' object has no attribute 'key'. Did you mean: 'keys'?
k.keys()
   
dict_keys(['karnataka', 'andra pradesh', 'madhya pradesh', 'karnatak'])
k.values()
   
dict_values(['bangalore', 'amaravati', 'bhopal', 'bangalore'])
k.items()
   
dict_items([('karnataka', 'bangalore'), ('andra pradesh', 'amaravati'), ('madhya pradesh', 'bhopal'), ('karnatak', 'bangalore')])
m='common'
   
print(dict(m))
   
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    print(dict(m))
ValueError: dictionary update sequence element #0 has length 1; 2 is required
