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
m='action'
n='pro'+m[3]
print(n)
proi
n='pro'+m[:2]
print(n)
proac
n='pro'+m[:3]
print(n)
proact
a=n[2]=o
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
y=a.find('@')
print(y)
-1
y=x.find('@')
print(y)
46
z=x.find('',d)
z=x.find('','d')
z=x.find('':'d')
z=x.find('')
print(z)
0
k=x.find[y+1:6]
k=x[y+1:5]
print (k)
print(k)
y=x.find['','t']
y=x.find['@':'t']
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
a.insert('vani','ravi')
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
a=['ramesh', 'suresh', 'ravi', 'ganesh', 'vani'] 
a.pop()
   
'vani'
del a[:3]
print(a)
['ganesh']
a.extend['rani']
a.extend('rani') 
print(a)  
['ganesh', 'r', 'a', 'n', 'i']
print(min(a))
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
[0, 9, 12, 25, 34, 50, 56, 67, 82]
>>> n.count(3)
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
