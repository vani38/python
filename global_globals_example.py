a=10
print(id(a))
def some():
    global a
    a=9
    print(id(a))
    print(a)
some()
print(a)
#same id
a=10
def some():
    global a
    a=9
    print(id(a))
    print(a)
print(id(a))
some()
print(a)
#globals
a=10
print(id(a))
def some():
    a=9
    x=globals()['a']
    print(id(x))
    print(x)
    globals()['a']=15
some()
print(id(a))
print(a)
