Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=[1,2,34,19,34,54,90,24,54,78]
b=sorted(a,reverse=True)
print(b)
[90, 78, 54, 54, 34, 34, 24, 19, 2, 1]
a.count(54)
2
set(a)
{1, 2, 34, 78, 19, 54, 24, 90}
[a]\]
a[0]

1
a[-5]
   
23
a[0:4:2]
   
(1, 4)
a[4:2:-1]
   
(36, 456)
a.count(1)
   
1
(a,b,c)=([1,2],'ram',5.6)
   
print(a)
   
[1, 2]
a,b=5,6
   
a,b=b,a
   
print(a)
   
6

a={1,2,3,4,4,5,6,7,8,9,10}
   
print(a)
   
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(a)
   
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
b={1,12,2,3,2,342,2,3,5,3,5,78,98,8,8,9,10,10,23,23,4,3,43,44,54,54,54,78}
   
print(b)
   
{1, 2, 3, 4, 5, 8, 9, 10, 12, 78, 342, 23, 98, 43, 44, 54}
print(b)
   
{1, 2, 3, 4, 5, 8, 9, 10, 12, 78, 342, 23, 98, 43, 44, 54}
print(b)
   
{1, 2, 3, 4, 5, 8, 9, 10, 12, 78, 342, 23, 98, 43, 44, 54}
{1, 2, 3, 4, 5, 8, 9, 10, 12, 78, 342, 23, 98, 43, 44, 54}
   
{1, 2, 3, 4, 5, 8, 9, 10, 12, 78, 342, 23, 98, 43, 44, 54}
a={1:'ram',None:'dev','sita':5.6}
   
a.get(None)
   
'dev'
a.get(3)
   
a.get(3,'not found')
   
'not found'
k=['bng','chn','mum']
   
v=['kar','tn','mh']
   
y=zip(k,v)
   
print
   
<built-in function print>
a={}
   
type{}
   
SyntaxError: invalid syntax
type(a)
   
<class 'dict'>
y=dict(zip(k,v))
   
print(y)
   
{'bng': 'kar', 'chn': 'tn', 'mum': 'mh'}
y=['hyd']='tel'
   
SyntaxError: cannot assign to literal
y=['hyd']='tel'
   
SyntaxError: cannot assign to literal
y['bng']='mp'
   
print(y)
   
{'bng': 'mp', 'chn': 'tn', 'mum': 'mh'}
>>> y=['hyd']='tel'
...    
SyntaxError: cannot assign to literal
>>> y['hyd']='tel'
...    
>>> print(y)
...    
{'bng': 'mp', 'chn': 'tn', 'mum': 'mh', 'hyd': 'tel'}
>>> type(y)
...    
<class 'dict'>
>>> p={'tn':'chen','kochi':3510,'kar':{'bng':'rajajinagar','mys':'vijaynagar'},'hyd':[madhapura,(charminar)}
...    
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> p={'tn':'chen','kochi':3510,'kar':{'bng':'rajajinagar','mys':'vijaynagar'},'hyd':['madhapura','charminar')}
...    
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> p={'tn':'chen','kochi':3510,'kar':{'bng':'rajajinagar','mys':'vijaynagar'},'hyd':['madhapura','charminar']}
...    
>>> y={'name':['ram','sita','dev'],'age':[25,23,27]}
...    
>>> type(y)
...    
<class 'dict'>
>>>  purse=dict()
...    
SyntaxError: unexpected indent
>>> purse=dict()
...    
>>> purse['money']=12
...    
>>> purse['candy']=3
...    
>>> purse['tissue']=75
...    
>>> print purse
...    
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> print(purse)
...    
{'money': 12, 'candy': 3, 'tissue': 75}
