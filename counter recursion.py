def g(i):
    print(i)
    i+=1
    g(i)
g(1)

#recursion
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
r=fact(4)
print(r)
