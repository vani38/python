#total variable are same
def total(g,h):
    s=g-h
    print(s)
total(50,15)
#if we given more values
def sum(x,*y):
    z=x
    for i in y:
        z=z+i
    print(z)
sum(10,20,30,40)    
