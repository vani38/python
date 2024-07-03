x=[5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
def number(x):
    even=0
    odd=0
    for a in x:
        if (a%2)==0:
            even+=1
        else:
            odd+=1
    return even,odd
y,z=number(x)
print('even',y)
print('odd',z)

