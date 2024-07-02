def topten():
    n=1
    while n<=10:
        cube=n*n*n
        yield cube
        n+=1
value=topten()
for i in value:
    print(i)
    