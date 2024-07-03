Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x='Besant Technology'
print(x[0:3])
Bes
print(x[0:4:2])
Bs
print(x[6:2:-1])
 tna
print(len(x))
17
print(x[20:10:2])

print(x[17:10:2])

print(x[17:10:-2])
yoo
print(x[17:1:-2])
yoohe ns
print(x[:])
Besant Technology
print(x[:7])
Besant 
#concatinate
x='Besant'
y='Technology'
print(x+y)
BesantTechnology
print(x+x[8:])
Besant
x=action
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    x=action
NameError: name 'action' is not defined
m='action'
n='pro'+m[3]
print n
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print(n)
proi
n='pro'+m[:2]
print(n)
proac
n='pro'+m[:3]
print(n)
proact
#in
print(n[2])=o
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
a=n[2]=o
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a=n[2]=o
NameError: name 'o' is not defined
n.startswith('p')
True
n.startswith('r')
False
n.upper()
'PROACT'
n.lower()
'proact'
n.find('a')
3
n.find('st')
-1
x='hi'
y='good morning'
z=y.replace('good','very good')
print (z)
very good morning
m=n.replace('pro','perfect')
print (m)
perfectact
a='       hello world       '
print(a.lstrip)
<built-in method lstrip of str object at 0x0000018A46458670>
print(a.lstrip())
hello world       
print(a.rstrip())
       hello world
print(a.strip())
hello world
x='I am Vani.I have completed my post graduation @ 2020.I have 2 years experience in teaching field'
y=a.find(@)
SyntaxError: invalid syntax
y=a.find('@')
print(y)
-1
y=x.find('@')
print(y)
46
z=x.find('',d)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    z=x.find('',d)
NameError: name 'd' is not defined. Did you mean: 'id'?
z=x.find('','d')
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    z=x.find('','d')
TypeError: slice indices must be integers or None or have an __index__ method
z=x.find('':'d')
SyntaxError: invalid syntax
z=x.find('')
print(z)
0
k=x.find[y+1:6]
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    k=x.find[y+1:6]
TypeError: 'builtin_function_or_method' object is not subscriptable
k=x[y+1:5]
print (k)

print(k)

y=x.find['',t]
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    y=x.find['',t]
NameError: name 't' is not defined
y=x.find['','t']
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    y=x.find['','t']
TypeError: 'builtin_function_or_method' object is not subscriptable
y=x.find['@':'t']
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    y=x.find['@':'t']
TypeError: 'builtin_function_or_method' object is not subscriptable
z=x.find('e',y)
print(z)
58
print(len(x))
96
u=x[y+1:6]
print(u)

v=x[y+1:3]
print(v)

a=['ramesh','suresh','ganesh']
b=['vani','rani','bhavani']
c=[a,b]
print(c)
[['ramesh', 'suresh', 'ganesh'], ['vani', 'rani', 'bhavani']]
a.append('vani')
print(a)
['ramesh', 'suresh', 'ganesh', 'vani']
a.insert('ravi')
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    a.insert('ravi')
TypeError: insert expected 2 arguments, got 1
a.insert('vani','ravi')
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    a.insert('vani','ravi')
TypeError: 'str' object cannot be interpreted as an integer
a.insert*('ganesh','ravi')
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    a.insert*('ganesh','ravi')
TypeError: can't multiply sequence by non-int of type 'builtin_function_or_method'
a.insert(2,'ravi')
print(a)
['ramesh', 'suresh', 'ravi', 'ganesh', 'vani']
a.remove('vani')
print(a)
['ramesh', 'suresh', 'ravi', 'ganesh']
a.clear()
print(a)
[]
a.clear('ravi')
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    a.clear('ravi')
TypeError: list.clear() takes no arguments (1 given)
a=[['ramesh', 'suresh', 'ravi', 'ganesh', 'vani']
a.pop()
   
SyntaxError: '[' was never closed
a=['ramesh', 'suresh', 'ravi', 'ganesh', 'vani']
   
a.pop()
   
'vani'
del.a[:3]
   
SyntaxError: invalid syntax
del a[:3]
   
print(a)
   
['ganesh']
a.extend['rani']
   
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    a.extend['rani']
TypeError: 'builtin_function_or_method' object is not subscriptable
a.extend('rani')
   
print(a)
   
['ganesh', 'r', 'a', 'n', 'i']
print(min(a))
   
a
a=['ramesh','suresh','ganesh','vani','rani']
   
print(min(a))
   
ganesh
a=[1,2,3,4,5,6,7,8,9,10]
   
print(sum(a))
   
55
print(len(a))
   
10
avg=sum(a)/len(a)
   
print(avg)
   
5.5
m=[50,56,34,67,82,12,9,0,25]
   
m.sort()
   
print(m)
...    
[0, 9, 12, 25, 34, 50, 56, 67, 82]
>>> n.count(50)
...    
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    n.count(50)
TypeError: must be str, not int
>>> n.count(3)
...    
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    n.count(3)
TypeError: must be str, not int
>>> m.count(3)
...    
0
>>> m.count(12)
...    
1
>>> x.split()
...    
['I', 'am', 'Vani.I', 'have', 'completed', 'my', 'post', 'graduation', '@', '2020.I', 'have', '2', 'years', 'experience', 'in', 'teaching', 'field']
>>> 
= RESTART: C:/Users/Administrator/AppData/Local/Programs/Python/Python312/practice 6.py
Bes
Besant Tec
yoohe ns
17
Besant Technology
proact
perfectact
Traceback (most recent call last):
  File "C:/Users/Administrator/AppData/Local/Programs/Python/Python312/practice 6.py", line 23, in <module>
    print(k.lstring())
AttributeError: 'str' object has no attribute 'lstring'. Did you mean: 'lstrip'?
