x="Besant Technology"
print(x[0:3])
print(x[0:10])
print(x[17:1:-2])
print(len(x))
print(x[:])
#concatinate
m='action'
n='pro'+m[:3]
print(n)
#in
n.startswith('p')
n.startswith('r')
#string library
n.upper()
n.lower()
n.find('a')
n.find('st')
m=n.replace('pro','perfect')
print(m)
#strip
k='       string      '
print(k.lstring())
print(k.rstring())
print(k.string())
#find
x='I am Vani.I have completed my post graduation @ 2020.I have 2 years experience in teaching field'
y=x.find('@')
print(y)
z=x.find('e',y)
print(z)
#list in list
a=['ramesh','suresh','ganesh']
b=['vani','rani','guni']
c=[a,b]
print(c)
#string library
a.append('vani')
print(a)
a.insert(3,'ravi')
print(a)
a.remove('vani')
print(a)
a.pop()
print(a)
del a[:3]
print(a)
a.extend('rani')
print(a)
print(min(a))
print(max(a))
a=[1,2,3,4,5,6,7,8,9,10]
print(sum(a))
print(len(a))
avg=sum(a)/len(a)
print(avg)
m=[50,25,47,59,10,30,27,0,21,65,81]
m.sort()
print(m)
m.count(0)
m.count(20)
m.index(59)
x.split()
