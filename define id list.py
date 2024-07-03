#def id for list
def share(y):
    print(id(y))
    y=[1000,500,200,100,300]
    print(id(y))
    print(y)
q=[400,600,700,100,800]
print(id(q))
share(q)
print(q)
