m=75
print(id(m))
def practice():
    m=10
    n=globals()['m']
    print(id(n))
    print(n)
    globals()['m']=20
practice()
print(id(m))
print(m)
